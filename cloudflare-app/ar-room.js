import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js";
const $=s=>document.querySelector(s);
const stage=$("#stage"),hint=$("#stageHint"),status=$("#status"),camera=$("#camera");
let renderer,scene,camera3d,model,session,hitSource,refSpace,previewStream,previewMode=false,dragging=false,lastX=0,lastY=0,dragStartX=0,dragStartY=0;

const catalogue={
 atom:{title:"Structure of an Atom",subject:"CHEMISTRY",grade:"Class 9",info:"A simplified atomic model. The nucleus contains protons and neutrons; electrons occupy regions around it. Electron paths are illustrative, not literal planetary orbits.",facts:["Nucleus: protons (+) and neutrons (0).","Electrons carry negative charge (−).","Most of an atom's volume is the electron cloud."],kind:"atom"},
 circuit:{title:"Electric Circuit",subject:"PHYSICS",grade:"Class 6",info:"A cell, connecting wires, switch and bulb form a simple series circuit. Toggle the switch to observe how a complete path allows current to flow.",facts:["A closed conducting path is needed for current.","The cell converts chemical energy to electrical energy.","The bulb converts electrical energy mainly to light and heat."],kind:"circuit"},
 magnetic:{title:"Magnetic Field Around a Bar Magnet",subject:"PHYSICS",grade:"Class 10",info:"Explore a bar magnet and the surrounding magnetic field. The field lines form continuous closed loops; outside the magnet they run from north to south.",facts:["Outside the magnet: N → S.","Inside the magnet: S → N.","Field lines never cross one another."],kind:"magnetic"},
 refraction:{title:"Refraction Through a Glass Block",subject:"PHYSICS",grade:"Class 9",info:"A light ray changes direction when it passes between air and glass because its speed changes. The ray bends towards the normal on entering glass.",facts:["Air to glass: bends towards the normal.","Glass to air: bends away from the normal.","The emergent ray is parallel to the incident ray for a parallel-sided block."],kind:"refraction"},
 cell:{title:"Plant Cell: Structure and Organelles",subject:"BIOLOGY",grade:"Class 9",info:"Explore a simplified plant cell with a cell wall, cell membrane, cytoplasm, nucleus, chloroplasts and a large central vacuole.",facts:["Cell wall provides support and protection.","Chloroplasts contain chlorophyll for photosynthesis.","The nucleus contains genetic material and helps control cell activities."],kind:"cell"}
};

const material=(color,extra={})=>new THREE.MeshStandardMaterial({color,roughness:.42,metalness:.08,...extra});
function label(text,color="#eaf7ff"){
 const c=document.createElement("canvas"),ctx=c.getContext("2d");c.width=512;c.height=128;
 ctx.fillStyle="rgba(4,20,37,.88)";ctx.strokeStyle="rgba(111,220,235,.9)";ctx.lineWidth=5;
 ctx.beginPath();ctx.roundRect(5,5,502,118,22);ctx.fill();ctx.stroke();
 ctx.font="bold 42px system-ui";ctx.fillStyle=color;ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(text,256,66);
 const texture=new THREE.CanvasTexture(c),sprite=new THREE.Sprite(new THREE.SpriteMaterial({map:texture,transparent:true,depthTest:false}));
 sprite.scale.set(1.05,.26,1);sprite.userData.isLabel=true;return sprite;
}
function tube(group,points,color,r=.012){
 const curve=new THREE.CatmullRomCurve3(points.map(p=>new THREE.Vector3(...p)));
 const mesh=new THREE.Mesh(new THREE.TubeGeometry(curve,48,r,8,false),new THREE.MeshBasicMaterial({color}));
 group.add(mesh);return mesh;
}
function makeAtom(g){
 const sphere=(r,color,x,y,z)=>{const m=new THREE.Mesh(new THREE.SphereGeometry(r,32,24),material(color,{emissive:color,emissiveIntensity:.08}));m.position.set(x,y,z);g.add(m);return m;};
 sphere(.17,0xffa64d,0,0,0);sphere(.12,0x5bc9ef,.09,.08,.02);sphere(.11,0xe87991,-.1,-.06,.04);
 const core=label("NUCLEUS");core.position.set(0,.34,0);g.add(core);
 for(let i=0;i<3;i++){const ring=new THREE.Mesh(new THREE.TorusGeometry(.62+i*.12,.009,8,100),new THREE.MeshBasicMaterial({color:[0x66d9ef,0x7fe2b2,0xb89aff][i]}));ring.rotation.set(i*.9,.4+i*.7,0);g.add(ring);const e=sphere(.055,0x7ee6bd,Math.cos(i*2)*(.62+i*.12),Math.sin(i*2)*(.62+i*.12),.08);e.userData.orbit=i;}
}
function makeCircuit(g){
 const dark=material(0x18334a),copper=material(0xd98b45,{metalness:.78,roughness:.28}),red=material(0xe65d58),blue=material(0x4f9be8),metal=material(0xc4d1dc),glass=new THREE.MeshPhysicalMaterial({color:0xffe8a6,emissive:0xffbd45,emissiveIntensity:.04,transparent:true,opacity:.58,roughness:.12});
 const box=(w,h,d,m,x,y,z)=>{const o=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);o.position.set(x,y,z);g.add(o);return o;};
 const cyl=(rt,rb,h,m,x,y,z)=>{const o=new THREE.Mesh(new THREE.CylinderGeometry(rt,rb,h,28),m);o.position.set(x,y,z);g.add(o);return o;};
 box(2.35,.09,1.48,dark,0,-.055,0);
 cyl(.19,.19,.62,material(0x397fc2),-.83,.34,0);cyl(.195,.195,.035,material(0x1b2c3c),-.83,.66,0);cyl(.075,.075,.075,copper,-.83,.715,0);
 box(.025,.105,.018,metal,-.83,.43,.196);box(.085,.025,.018,metal,-.83,.43,.196);box(.085,.025,.018,metal,-.83,.24,.196);
 cyl(.17,.19,.12,material(0x34495e),.82,.10,0);cyl(.105,.105,.20,metal,.82,.25,0);
 for(let i=0;i<3;i++)cyl(.112,.112,.018,copper,.82,.19+i*.055,0);
 const dome=new THREE.Mesh(new THREE.SphereGeometry(.19,28,22,0,Math.PI*2,0,Math.PI*.72),glass);dome.position.set(.82,.47,0);g.add(dome);
 tube(g,[[.82,.32,0],[.77,.43,0],[.82,.52,0],[.87,.43,0]],0xd98b45,.012);
 box(.48,.045,.34,material(0x28465e),0,.045,-.48);cyl(.055,.055,.10,copper,-.18,.13,-.48);cyl(.055,.055,.10,copper,.18,.13,-.48);
 const lever=new THREE.Mesh(new THREE.BoxGeometry(.38,.045,.065),metal);lever.position.set(0,.25,-.48);lever.rotation.z=-.18;g.add(lever);
 const pivot=new THREE.Mesh(new THREE.SphereGeometry(.065,18,14),copper);pivot.position.set(-.18,.17,-.48);g.add(pivot);
 tube(g,[[-.83,.70,0],[-.83,.79,-.48],[-.18,.20,-.48]],0xe65d58,.025);
 tube(g,[[.18,.20,-.48],[.48,.22,-.48],[.82,.30,-.22],[.82,.30,0]],0xe65d58,.025);
 tube(g,[[.82,.30,0],[.82,.79,.55],[0,.79,.62],[-.83,.70,.18]],0x4f9be8,.025);
 const glow=new THREE.PointLight(0xffc35b,0,.9);glow.position.set(.82,.52,0);g.add(glow);
 g.userData={kind:"circuit",bulbMaterial:glass,bulbGlow:glow,lever,circuitOn:true};setCircuitState(true,g);
 const l=label("CELL  •  SWITCH  •  BULB");l.position.set(0,.98,0);g.add(l);
}
function makeMagnetic(g){
 const magnet=new THREE.Mesh(new THREE.BoxGeometry(1.55,.34,.38),material(0x245b9a,{metalness:.28}));g.add(magnet);
 const n=new THREE.Mesh(new THREE.BoxGeometry(.76,.36,.4),material(0xd94e55));n.position.x=-.395;g.add(n);
 const s=new THREE.Mesh(new THREE.BoxGeometry(.76,.36,.4),material(0x397fd0));s.position.x=.395;g.add(s);
 const nl=label("N", "#ffd9d9");nl.scale.set(.32,.22,1);nl.position.set(-.4,.25,0);g.add(nl);
 const sl=label("S");sl.scale.set(.32,.22,1);sl.position.set(.4,.25,0);g.add(sl);
 // Closed-loop field lines: outer arcs return through the magnet's interior.
 for(let i=0;i<5;i++){
  const y=.18+i*.16,z=(i-2)*.13, lift=.48+i*.13;
  tube(g,[[-.78,y,z],[-.88,lift,z],[-.48,lift+.18,z],[0,lift+.22,z],[.48,lift+.18,z],[.88,lift,z],[.78,y,z]],0x62d9f2,.009);
  tube(g,[[.78,y,z],[.48,-.2-i*.025,z],[0,-.23-i*.025,z],[-.48,-.2-i*.025,z],[-.78,y,z]],0x62d9f2,.009);
 }
 const note=label("FIELD LINES: N → S OUTSIDE");note.scale.set(1.5,.25,1);note.position.set(0,.95,.05);g.add(note);
}
function makeRefraction(g){
 const glass=new THREE.Mesh(new THREE.BoxGeometry(1.18,.78,.42),new THREE.MeshPhysicalMaterial({color:0x75c9ef,transparent:true,opacity:.2,roughness:.08,metalness:0,side:THREE.DoubleSide}));g.add(glass);
 const edges=new THREE.LineSegments(new THREE.EdgesGeometry(glass.geometry),new THREE.LineBasicMaterial({color:0x8fe5ff}));g.add(edges);
 // Incident, refracted and emergent ray, drawn in the front plane for clear observation.
 tube(g,[[-1.12,.53,.28],[-.59,.28,.28]],0xffc95e,.018);
 tube(g,[[-.59,.28,.28],[.15,.04,.28]],0xffc95e,.018);
 tube(g,[[.15,.04,.28],[1.12,-.28,.28]],0xffc95e,.018);
 const normal1=new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(-.59,-.48,.31),new THREE.Vector3(-.59,.72,.31)]),new THREE.LineDashedMaterial({color:0xe7f5ff,dashSize:.06,gapSize:.04}));normal1.computeLineDistances();g.add(normal1);
 const normal2=new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(.59,-.48,.31),new THREE.Vector3(.59,.72,.31)]),new THREE.LineDashedMaterial({color:0xe7f5ff,dashSize:.06,gapSize:.04}));normal2.computeLineDistances();g.add(normal2);
 const a=label("AIR");a.scale.set(.45,.2,1);a.position.set(-.9,-.03,.34);g.add(a);
 const b=label("GLASS BLOCK");b.scale.set(.95,.2,1);b.position.set(0,.55,.34);g.add(b);
 const c=label("AIR");c.scale.set(.45,.2,1);c.position.set(.9,-.03,.34);g.add(c);
}
function makeCell(g){
 const wall=new THREE.Mesh(new THREE.BoxGeometry(1.8,1.05,.82),material(0x7acb79,{transparent:true,opacity:.2,side:THREE.DoubleSide}));g.add(wall);
 const edge=new THREE.LineSegments(new THREE.EdgesGeometry(wall.geometry),new THREE.LineBasicMaterial({color:0x83e59a}));g.add(edge);
 const membrane=new THREE.Mesh(new THREE.BoxGeometry(1.68,.93,.72),material(0x63b8a1,{transparent:true,opacity:.14,side:THREE.DoubleSide}));g.add(membrane);
 const vac=new THREE.Mesh(new THREE.BoxGeometry(.72,.65,.48),material(0x65b9e8,{transparent:true,opacity:.48}));vac.position.set(.25,-.05,0);g.add(vac);
 const nucleus=new THREE.Mesh(new THREE.SphereGeometry(.22,32,24),material(0xb38be8));nucleus.position.set(-.48,.1,.08);g.add(nucleus);
 const nucleolus=new THREE.Mesh(new THREE.SphereGeometry(.08,24,18),material(0x684a9c));nucleolus.position.set(-.45,.1,.25);g.add(nucleolus);
 for(let i=0;i<7;i++){const chlor=new THREE.Mesh(new THREE.SphereGeometry(.085,20,16),material(0x3fbd73));chlor.scale.set(1.35,.72,.75);chlor.position.set(-.62+(i%3)*.48,-.32+Math.floor(i/3)*.3,.2);g.add(chlor);}
 const mitoMat=material(0xe7a45c);for(let i=0;i<3;i++){const m=new THREE.Mesh(new THREE.SphereGeometry(.11,20,14),mitoMat);m.scale.set(1.7,.75,.8);m.position.set(-.12+i*.35,.34,.18);g.add(m);}
 const labels=[["CELL WALL",-.1,.72,.0],["NUCLEUS",-.82,.42,.2],["LARGE VACUOLE",.3,-.53,.2],["CHLOROPLASTS",.55,.43,.2]];
 labels.forEach(([t,x,y,z])=>{const l=label(t);l.scale.set(.82,.2,1);l.position.set(x,y,z);g.add(l);});
}
function makeModel(kind){const g=new THREE.Group();if(kind==="atom")makeAtom(g);else if(kind==="circuit")makeCircuit(g);else if(kind==="magnetic")makeMagnetic(g);else if(kind==="refraction")makeRefraction(g);else if(kind==="cell")makeCell(g);return g;}
function setCircuitState(on,target=model){if(!target||target.userData?.kind!=="circuit")return;target.userData.circuitOn=!!on;target.userData.bulbMaterial.emissiveIntensity=on?.95:.035;target.userData.bulbMaterial.emissive.setHex(on?0xffa92e:0x3b2b16);target.userData.bulbGlow.intensity=on?1.8:0;target.userData.lever.rotation.z=on?0:-.48;}
function setup(){if(renderer)return;renderer=new THREE.WebGLRenderer({alpha:true,antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.setSize(stage.clientWidth,stage.clientHeight);renderer.xr.enabled=true;stage.appendChild(renderer.domElement);scene=new THREE.Scene();camera3d=new THREE.PerspectiveCamera(55,stage.clientWidth/stage.clientHeight,.01,30);scene.add(new THREE.HemisphereLight(0xffffff,0x34516b,2));const light=new THREE.DirectionalLight(0xffffff,2);light.position.set(1,3,2);scene.add(light);changeModel();renderer.setAnimationLoop(()=>renderer.render(scene,camera3d));window.addEventListener("resize",resize);}
function resize(){if(!renderer)return;renderer.setSize(stage.clientWidth,stage.clientHeight);camera3d.aspect=stage.clientWidth/stage.clientHeight;camera3d.updateProjectionMatrix();}
function changeModel(){if(!scene)return;if(model)scene.remove(model);const id=$("#modelSelect").value,d=catalogue[id];model=makeModel(d.kind);scene.add(model);model.position.set(0,0,-2);$("#modelTitle").textContent=d.title;$("#modelInfo").textContent=d.info;$("#modelMeta").textContent=d.subject+"  •  "+d.grade;$("#modelFacts").innerHTML=d.facts.map(x=>"<li>"+x+"</li>").join("");}
async function startAR(){setup();if(!navigator.xr){status.textContent="WebXR AR is unavailable in this browser. Try Camera Preview.";return;}try{if(!await navigator.xr.isSessionSupported("immersive-ar")){status.textContent="This device/browser does not support immersive AR. Try Camera Preview.";return;}session=await navigator.xr.requestSession("immersive-ar",{requiredFeatures:["hit-test"],optionalFeatures:["local-floor","dom-overlay"],domOverlay:{root:document.body}});let refType=null;for(const candidate of ["local-floor","local"]){try{refSpace=await session.requestReferenceSpace(candidate);refType=candidate;break;}catch(_){}}if(!refType)throw new Error("No supported local reference space was found.");renderer.xr.setReferenceSpaceType(refType);await renderer.xr.setSession(session);const viewer=await session.requestReferenceSpace("viewer");hitSource=await session.requestHitTestSource({space:viewer});const reticle=new THREE.Mesh(new THREE.RingGeometry(.08,.11,32),new THREE.MeshBasicMaterial({color:0x70edbd,side:THREE.DoubleSide}));reticle.rotation.x=-Math.PI/2;reticle.matrixAutoUpdate=false;reticle.visible=false;scene.add(reticle);let placed=false;const controller=renderer.xr.getController(0);scene.add(controller);const raycaster=new THREE.Raycaster();controller.addEventListener("select",()=>{if(model?.userData.kind==="circuit"){raycaster.setFromXRController(controller);if(raycaster.intersectObject(model.userData.lever).length){setCircuitState(!model.userData.circuitOn,model);status.textContent=model.userData.circuitOn?"Switch closed: bulb ON.":"Switch open: bulb OFF.";return;}}if(reticle.visible){model.position.setFromMatrixPosition(reticle.matrix);model.quaternion.setFromRotationMatrix(reticle.matrix);placed=true;status.textContent="Model placed. Move around it to observe different sides.";}});renderer.setAnimationLoop((time,frame)=>{if(frame&&hitSource){const hits=frame.getHitTestResults(hitSource);if(hits.length){const pose=hits[0].getPose(refSpace);reticle.visible=true;reticle.matrix.fromArray(pose.transform.matrix);if(!placed){model.position.setFromMatrixPosition(reticle.matrix);model.quaternion.setFromRotationMatrix(reticle.matrix);}}else reticle.visible=false;}renderer.render(scene,camera3d);});session.addEventListener("end",()=>{session=null;hitSource=null;reticle.visible=false;document.body.classList.remove("ar-active");resize();renderer.setAnimationLoop(()=>renderer.render(scene,camera3d));status.textContent="AR session ended.";$("#stopAR").disabled=true;});$("#stopAR").disabled=false;$("#placeModel").disabled=false;$("#rotateModel").disabled=false;hint.hidden=true;document.body.classList.add("ar-active");resize();status.textContent="Move your phone slowly to find a surface. Tap to place the model.";}catch(e){if(session){try{await session.end();}catch(_){}session=null;}hitSource=null;refSpace=null;status.textContent="Could not start true surface AR: "+(e.message||"AR setup failed")+". Camera Preview remains available.";}}
async function startPreview(){setup();previewMode=true;try{previewStream=await navigator.mediaDevices.getUserMedia({video:{facingMode:{ideal:"environment"}},audio:false});camera.srcObject=previewStream;await camera.play();document.body.classList.add("preview-active");camera.style.display="block";stage.style.background="transparent";hint.hidden=true;renderer.setAnimationLoop(()=>renderer.render(scene,camera3d));model.position.set(0,0,-2);status.textContent="Camera preview shows a draggable 3D model overlay; it does not automatically detect surfaces.";$("#placeModel").disabled=false;$("#rotateModel").disabled=false;$("#stopAR").disabled=false;}catch(e){status.textContent="Camera access was not granted. Allow camera permission and reload.";}}
$("#modelSelect").addEventListener("change",changeModel);$("#startAR").addEventListener("click",startAR);$("#cameraMode").addEventListener("click",startPreview);$("#rotateModel").addEventListener("click",()=>{if(model)model.rotation.y+=Math.PI/4;});$("#placeModel").addEventListener("click",()=>{if(model){model.position.set(0,0,-2);model.rotation.set(0,0,0);status.textContent="Model reset to the view."; }});
$("#stopAR").addEventListener("click",async()=>{if(session)await session.end();if(previewStream){previewStream.getTracks().forEach(t=>t.stop());previewStream=null;}camera.style.display="none";document.body.classList.remove("ar-active","preview-active");resize();previewMode=false;$("#stopAR").disabled=true;$("#placeModel").disabled=true;$("#rotateModel").disabled=true;hint.hidden=false;status.textContent="Experience ended.";});
setup();renderer.domElement.style.touchAction="none";renderer.domElement.addEventListener("pointerdown",e=>{if(!previewMode&&!session)return;dragging=true;lastX=e.clientX;lastY=e.clientY;dragStartX=e.clientX;dragStartY=e.clientY;renderer.domElement.setPointerCapture?.(e.pointerId);});renderer.domElement.addEventListener("pointermove",e=>{if(!dragging||!model)return;model.rotation.y+=(e.clientX-lastX)*.009;model.rotation.x+=(e.clientY-lastY)*.006;lastX=e.clientX;lastY=e.clientY;});renderer.domElement.addEventListener("pointerup",e=>{if(dragging&&model?.userData.kind==="circuit"&&Math.hypot(e.clientX-dragStartX,e.clientY-dragStartY)<8&&!session){const r=renderer.domElement.getBoundingClientRect(),p=new THREE.Vector2(((e.clientX-r.left)/r.width)*2-1,-((e.clientY-r.top)/r.height)*2+1),ray=new THREE.Raycaster();ray.setFromCamera(p,camera3d);if(ray.intersectObject(model.userData.lever).length)setCircuitState(!model.userData.circuitOn,model);}dragging=false;});renderer.domElement.addEventListener("pointercancel",()=>dragging=false);
