import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js";
const $=s=>document.querySelector(s), stage=$("#stage"), hint=$("#stageHint"), status=$("#status"), camera=$("#camera"), overlay=$("#overlay");
let renderer,scene,camera3d,model,session,hitSource,refSpace,previewStream,previewMode=false,turn=0,circuitOn=true,dragging=false,lastX=0,lastY=0,dragStartX=0,dragStartY=0;
const descriptions={atom:["Structure of an Atom","A simplified atom model: a central nucleus contains protons and neutrons, while electrons occupy regions around it."],circuit:["Electric Circuit","A simplified closed circuit contains a cell, connecting wires, a switch and a bulb. The bulb glows when the path is complete."],solar:["Solar System","Explore a simplified arrangement of the Sun and planets. Distances and sizes are not to scale."]};
function makeModel(kind){
 const group=new THREE.Group();
 const mat=(color,emissive=color)=>new THREE.MeshStandardMaterial({color,roughness:.35,metalness:.12,emissive,emissiveIntensity:.16});
 const sphere=(r,color,x,y,z)=>{const m=new THREE.Mesh(new THREE.SphereGeometry(r,32,24),mat(color));m.position.set(x,y,z);group.add(m);return m};
 const line=(points,color=0x8bd8ef)=>{const g=new THREE.BufferGeometry().setFromPoints(points.map(p=>new THREE.Vector3(...p)));group.add(new THREE.Line(g,new THREE.LineBasicMaterial({color})))};
 if(kind==="atom"){
  sphere(.16,0xffad4d,0,0,0);sphere(.12,0x62d8ed,.09,.08,0);sphere(.11,0xf36b85,-.1,-.06,.04);
  for(let i=0;i<3;i++){const ring=new THREE.Mesh(new THREE.TorusGeometry(.62+i*.12,.009,8,100),new THREE.MeshBasicMaterial({color:[0x66d9ef,0x7fe2b2,0xb89aff][i]}));ring.rotation.set(i*.9,.4+i*.7,0);group.add(ring);const e=sphere(.055,0x7ee6bd,Math.cos(i*2)*(.62+i*.12),Math.sin(i*2)*(.62+i*.12),.08);e.userData.orbit=i;}
 }else if(kind==="circuit"){
  // School-lab series circuit: cell, insulated connecting leads, key and an incandescent-style bulb.
  const dark=mat(0x263b50),copper=new THREE.MeshStandardMaterial({color:0xd98b45,metalness:.78,roughness:.28}),redWire=new THREE.MeshStandardMaterial({color:0xe65d58,roughness:.48}),blueWire=new THREE.MeshStandardMaterial({color:0x4f9be8,roughness:.48}),metal=mat(0xc4d1dc),glass=new THREE.MeshPhysicalMaterial({color:0xffe8a6,emissive:0xffbd45,emissiveIntensity:.04,transparent:true,opacity:.58,roughness:.12,metalness:0});
  const box=(w,h,d,material,x,y,z)=>{const m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),material);m.position.set(x,y,z);group.add(m);return m;};
  const cylinder=(rt,rb,h,material,x,y,z,rot=0)=>{const m=new THREE.Mesh(new THREE.CylinderGeometry(rt,rb,h,28),material);m.position.set(x,y,z);m.rotation.z=rot;group.add(m);return m;};
  const wire=(pts,material)=>{const curve=new THREE.CatmullRomCurve3(pts.map(p=>new THREE.Vector3(...p)));const m=new THREE.Mesh(new THREE.TubeGeometry(curve,36,.025,8,false),material);group.add(m);return m;};
  // Low-profile insulated demonstration board.
  const board=box(2.35,.09,1.48,dark,0,-.055,0);board.material.color.setHex(0x18334a);
  // Cell body and clearly marked terminals.
  cylinder(.19,.19,.62,mat(0x397fc2),-.83,.34,0);
  cylinder(.195,.195,.035,mat(0x1b2c3c),-.83,.66,0);
  cylinder(.075,.075,.075,copper,-.83,.715,0);
  cylinder(.075,.075,.075,metal,-.83,.715,.18);
  // Raised polarity marks on the visible face of the cell.
  box(.025,.105,.018,metal,-.83,.43,.196);
  box(.085,.025,.018,metal,-.83,.43,.196);
  box(.085,.025,.018,metal,-.83,.24,.196);
  // Bulb holder, metal screw base, glass envelope and visible filament.
  cylinder(.17,.19,.12,mat(0x34495e),.82,.10,0);
  cylinder(.105,.105,.20,metal,.82,.25,0);
  for(let i=0;i<3;i++)cylinder(.112,.112,.018,copper,.82,.19+i*.055,0);
  const dome=new THREE.Mesh(new THREE.SphereGeometry(.19,28,22,0,Math.PI*2,0,Math.PI*.72),glass);dome.position.set(.82,.47,0);group.add(dome);
  const filament=wire([[.82,.32,0],[.77,.43,0],[.82,.52,0],[.87,.43,0]],copper);filament.userData.isFilament=true;
  // Open knife key with two terminals and a hinged lever.
  box(.48,.045,.34,mat(0x28465e),0,.045,-.48);
  cylinder(.055,.055,.10,copper,-.18,.13,-.48);
  cylinder(.055,.055,.10,copper,.18,.13,-.48);
  const lever=new THREE.Mesh(new THREE.BoxGeometry(.38,.045,.065),mat(0xd9e2e9));lever.position.set(0,.25,-.48);lever.rotation.z=-.18;group.add(lever);
  const pivot=new THREE.Mesh(new THREE.SphereGeometry(.065,18,14),copper);pivot.position.set(-.18,.17,-.48);group.add(pivot);
  // Continuous leads: cell -> key -> bulb -> cell. The key visibly opens/closes the circuit.
  wire([[-.83,.70,0],[-.83,.79,-.48],[-.18,.20,-.48]],redWire);
  wire([[.18,.20,-.48],[.48,.22,-.48],[.82,.30,-.22],[.82,.30,0]],redWire);
  wire([[.82,.30,0],[.82,.79,.55],[0,.79,.62],[-.83,.70,.18]],blueWire);
  // Small terminal caps and plus/minus markings as simple raised symbols.
  box(.12,.025,.12,metal,-.83,.79,0);
  const bulbGlow=new THREE.PointLight(0xffc35b,0,.9);bulbGlow.position.set(.82,.52,0);group.add(bulbGlow);
  group.userData={kind:"circuit",bulbMaterial:glass,bulbGlow,lever,filament,circuitOn:true};
  setCircuitState(true,group);
 }else{
  sphere(.23,0xffb84d,0,0,0);
  const planets=[[.42,.045,0x9aa7b5],[.62,.07,0xe6b36c],[.88,.08,0x4b9de2],[1.15,.065,0xe17d62],[1.52,.15,0xd9b77b],[1.9,.13,0xd5c49b],[2.22,.1,0x76cbd2],[2.5,.095,0x477bd0]];
  planets.forEach((p,i)=>{const orbit=new THREE.Mesh(new THREE.TorusGeometry(p[0],.004,6,120),new THREE.MeshBasicMaterial({color:0x6388a5}));orbit.rotation.x=Math.PI/2;group.add(orbit);sphere(p[1],p[2],p[0],0,0);});
 }
 return group;
}
function setCircuitState(on,target=model){
 if(!target||target.userData?.kind!=="circuit")return;
 target.userData.circuitOn=!!on;
 target.userData.bulbMaterial.emissiveIntensity=on ? 0.95 : 0.035;
 target.userData.bulbMaterial.emissive.setHex(on?0xffa92e:0x3b2b16);
 target.userData.bulbGlow.intensity=on?1.8:0;
 target.userData.lever.rotation.z=on?0:-.48;
 circuitOn=!!on;
}
function setup(){
 if(renderer)return;
 renderer=new THREE.WebGLRenderer({alpha:true,antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.setSize(stage.clientWidth,stage.clientHeight);renderer.xr.enabled=true;stage.appendChild(renderer.domElement);
 scene=new THREE.Scene();camera3d=new THREE.PerspectiveCamera(55,stage.clientWidth/stage.clientHeight,.01,30);
 scene.add(new THREE.HemisphereLight(0xffffff,0x34516b,2));const light=new THREE.DirectionalLight(0xffffff,2);light.position.set(1,3,2);scene.add(light);
 model=makeModel($("#modelSelect").value);scene.add(model);model.position.set(0,0,-2);
 renderer.setAnimationLoop(()=>{if(model&&!session){model.rotation.y+=.004;if($("#modelSelect").value==="atom")model.rotation.z+=.002;}renderer.render(scene,camera3d);});
 window.addEventListener("resize",resize);
}
function resize(){if(!renderer)return;renderer.setSize(stage.clientWidth,stage.clientHeight);camera3d.aspect=stage.clientWidth/stage.clientHeight;camera3d.updateProjectionMatrix();}
function changeModel(){if(model)scene.remove(model);model=makeModel($("#modelSelect").value);scene.add(model);model.position.set(0,0,-2);const d=descriptions[$("#modelSelect").value];$("#modelTitle").textContent=d[0];$("#modelInfo").textContent=d[1];if(model.userData.kind==="circuit")setCircuitState(true,model);}
async function startAR(){
 setup();
 if(!navigator.xr){status.textContent="WebXR AR is not available in this browser. Try Camera Preview.";return;}
 try{
  const supported=await navigator.xr.isSessionSupported("immersive-ar");
  if(!supported){status.textContent="This phone/browser does not support immersive AR. Try Camera Preview.";return;}
  session=await navigator.xr.requestSession("immersive-ar",{requiredFeatures:["hit-test"],optionalFeatures:["local-floor","dom-overlay"],domOverlay:{root:document.body}});
  // Pick a stable world reference space supported by this AR runtime before Three.js starts its XR renderer.
  let referenceType=null;
  for(const candidate of ["local-floor","local"]){
   try{refSpace=await session.requestReferenceSpace(candidate);referenceType=candidate;break;}catch(_){}
  }
  if(!referenceType)throw new Error("This AR runtime does not provide a stable local reference space for surface placement.");
  renderer.xr.setReferenceSpaceType(referenceType);
  await renderer.xr.setSession(session);
  const viewerSpace=await session.requestReferenceSpace("viewer");
  hitSource=await session.requestHitTestSource({space:viewerSpace});
  const reticle=new THREE.Mesh(new THREE.RingGeometry(.08,.11,32),new THREE.MeshBasicMaterial({color:0x70edbd,side:THREE.DoubleSide}));reticle.rotation.x=-Math.PI/2;reticle.matrixAutoUpdate=false;reticle.visible=false;scene.add(reticle);
  const controller=renderer.xr.getController(0);scene.add(controller);let placed=false;const xrRaycaster=new THREE.Raycaster();
  controller.addEventListener("select",()=>{
   if(model?.userData.kind==="circuit"&&model.userData.lever){xrRaycaster.setFromXRController(controller);const switchHits=xrRaycaster.intersectObject(model.userData.lever,true);if(switchHits.length){setCircuitState(!model.userData.circuitOn,model);status.textContent=model.userData.circuitOn?"Switch closed: bulb ON.":"Switch open: bulb OFF.";return;}}
   if(reticle.visible){model.position.setFromMatrixPosition(reticle.matrix);model.quaternion.setFromRotationMatrix(reticle.matrix);placed=true;status.textContent="Model placed. Walk around it or drag to rotate."; }
  });
  renderer.setAnimationLoop((time,frame)=>{if(frame&&hitSource){const hits=frame.getHitTestResults(hitSource);if(hits.length){const pose=hits[0].getPose(refSpace);reticle.visible=true;reticle.matrix.fromArray(pose.transform.matrix);if(!placed){model.position.setFromMatrixPosition(reticle.matrix);model.quaternion.setFromRotationMatrix(reticle.matrix);}}else reticle.visible=false;}renderer.render(scene,camera3d);});
  session.addEventListener("end",()=>{session=null;hitSource=null;reticle.visible=false;document.body.classList.remove("ar-active");resize();renderer.setAnimationLoop(()=>{if(model){model.rotation.y+=.004;}renderer.render(scene,camera3d);});status.textContent="AR session ended.";$("#stopAR").disabled=true;});
  $("#stopAR").disabled=false;$("#placeModel").disabled=false;$("#rotateModel").disabled=false;hint.hidden=true;document.body.classList.add("ar-active");resize();status.textContent="Move your phone slowly to find a surface. Tap the screen to place the model."; 
 }catch(e){
  if(session){try{await session.end();}catch(_){}session=null;}
  hitSource=null;refSpace=null;
  status.textContent="Could not start true surface AR: "+(e.message||"AR setup failed")+". Camera Preview remains available.";
 }
}
async function startPreview(){
 setup();previewMode=true;
 try{previewStream=await navigator.mediaDevices.getUserMedia({video:{facingMode:{ideal:"environment"}},audio:false});camera.srcObject=previewStream;await camera.play();document.body.classList.add("preview-active");camera.style.display="block";renderer.domElement.style.background="transparent";stage.style.background="transparent";hint.hidden=true;
 // Camera preview is a live camera view with a draggable 3D model overlay; it is not plane-tracked AR.
 renderer.setAnimationLoop(()=>{renderer.render(scene,camera3d);});model.position.set(0,0,-2);status.textContent="Camera preview is active. Drag on the 3D model area to rotate it. This preview does not automatically detect walls or floors.";
 $("#placeModel").disabled=false;$("#rotateModel").disabled=false;$("#stopAR").disabled=false;
 }catch(e){status.textContent="Camera access was not granted. Please allow camera permission and reload this page.";}}
$("#modelSelect").addEventListener("change",changeModel);
$("#startAR").addEventListener("click",startAR);
$("#cameraMode").addEventListener("click",startPreview);
$("#rotateModel").addEventListener("click",()=>{if(model)model.rotation.y+=Math.PI/4;});
$("#placeModel").addEventListener("click",()=>{if(model){model.position.set(0,0,-2);model.rotation.set(0,0,0);status.textContent="Model reset to the centre of the view."; }});
$("#stopAR").addEventListener("click",async()=>{if(session)await session.end();if(previewStream){previewStream.getTracks().forEach(t=>t.stop());previewStream=null;}camera.style.display="none";document.body.classList.remove("ar-active","preview-active");resize();previewMode=false;$("#stopAR").disabled=true;$("#placeModel").disabled=true;$("#rotateModel").disabled=true;hint.hidden=false;status.textContent="Experience ended.";});
setup();changeModel();
renderer.domElement.style.touchAction="none";
renderer.domElement.addEventListener("pointerdown",e=>{if(!previewMode&&!session)return;dragging=true;lastX=e.clientX;lastY=e.clientY;dragStartX=e.clientX;dragStartY=e.clientY;renderer.domElement.setPointerCapture?.(e.pointerId);});
renderer.domElement.addEventListener("pointermove",e=>{if(!dragging||!model)return;const dx=e.clientX-lastX,dy=e.clientY-lastY;if(Math.abs(dx)+Math.abs(dy)>2){model.rotation.y+=dx*.009;model.rotation.x+=dy*.006;}lastX=e.clientX;lastY=e.clientY;});
renderer.domElement.addEventListener("pointerup",e=>{if(dragging&&model?.userData.kind==="circuit"&&Math.hypot(e.clientX-dragStartX,e.clientY-dragStartY)<8&&!session){const rect=renderer.domElement.getBoundingClientRect();const pointer=new THREE.Vector2(((e.clientX-rect.left)/rect.width)*2-1,-((e.clientY-rect.top)/rect.height)*2+1);const ray=new THREE.Raycaster();ray.setFromCamera(pointer,camera3d);if(ray.intersectObject(model.userData.lever,true).length)setCircuitState(!model.userData.circuitOn,model);}dragging=false;});
renderer.domElement.addEventListener("pointercancel",()=>{dragging=false;});