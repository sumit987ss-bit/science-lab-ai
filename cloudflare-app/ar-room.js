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
 const c=document.createElement("canvas");c.width=768;c.height=160;const ctx=c.getContext("2d");
 ctx.fillStyle="rgba(4,20,37,.88)";ctx.strokeStyle="rgba(111,220,235,.9)";ctx.lineWidth=5;
 ctx.beginPath();ctx.roundRect(5,5,758,150,24);ctx.fill();ctx.stroke();
 const fontSize=Math.max(25,Math.min(40,Math.floor(700/(text.length*.57))));ctx.font="700 "+fontSize+"px Arial, sans-serif";ctx.fillStyle=color;ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(text,384,82,710);
 const texture=new THREE.CanvasTexture(c);texture.colorSpace=THREE.SRGBColorSpace;
 const sprite=new THREE.Sprite(new THREE.SpriteMaterial({map:texture,transparent:true,depthTest:true,depthWrite:false}));
 sprite.scale.set(1.18,.25,1);sprite.userData.isLabel=true;sprite.renderOrder=2;return sprite;
}
function tube(group,points,color,r=.012){
 const curve=new THREE.CatmullRomCurve3(points.map(p=>new THREE.Vector3(...p)));
 const mesh=new THREE.Mesh(new THREE.TubeGeometry(curve,48,r,8,false),new THREE.MeshBasicMaterial({color}));
 group.add(mesh);return mesh;
}
function callout(group,text,anchor,position,width=1.12){
 const a=new THREE.Vector3(...anchor),p=new THREE.Vector3(...position);
 const line=new THREE.Line(new THREE.BufferGeometry().setFromPoints([a,p]),new THREE.LineBasicMaterial({color:0x9bd9e8,transparent:true,opacity:.9,depthTest:true}));
 line.renderOrder=1;group.add(line);
 const dot=new THREE.Mesh(new THREE.SphereGeometry(.025,12,10),new THREE.MeshBasicMaterial({color:0x9bd9e8}));dot.position.copy(a);group.add(dot);
 const tag=label(text);tag.scale.set(width,width*.22,1);tag.position.copy(p);group.add(tag);return tag;
}
function makeAtom(g){
 const pMat=material(0xe95761,{emissive:0x421014,emissiveIntensity:.12});
 const nMat=material(0x4b91db,{emissive:0x102b51,emissiveIntensity:.12});
 const eMat=material(0x54dfc2,{emissive:0x105546,emissiveIntensity:.16});
 const particle=(tag,mat,r,pos,labelSize)=>{const ball=new THREE.Mesh(new THREE.SphereGeometry(r,32,24),mat);ball.position.set(...pos);g.add(ball);const textSprite=label(tag);textSprite.scale.set(labelSize,labelSize*.34,1);textSprite.position.set(pos[0],pos[1]+r+.075,pos[2]);g.add(textSprite);};
 particle("p+",pMat,.17,[-.18,0,0],.29);particle("n",nMat,.17,[.18,0,0],.27);
 const shell=(radius,color)=>{const ring=new THREE.Mesh(new THREE.TorusGeometry(radius,.012,10,128),new THREE.MeshBasicMaterial({color}));g.add(ring);};
 const inner=.62,outer=1.18;shell(inner,0x86c9ff);shell(outer,0x7ce5ba);
 [[inner,0,0],[-inner,0,0]].forEach(pos=>particle("e-",eMat,.075,pos,.20));
 for(let i=0;i<8;i++){const angle=i*Math.PI/4;particle("e-",eMat,.075,[outer*Math.cos(angle),outer*Math.sin(angle),0],.20);}
}
function makeCircuit(g){
 const baseMat=material(0x18334a),copper=material(0xd98b45,{metalness:.78,roughness:.28}),metal=material(0xc4d1dc),batteryMat=material(0x397fc2),dark=material(0x1b2c3c);
 const bulbGlass=new THREE.MeshPhysicalMaterial({color:0xffe8a6,emissive:0xffbd45,emissiveIntensity:.04,transparent:true,opacity:.58,roughness:.12});
 const box=(w,h,d,m,x,y,z)=>{const o=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);o.position.set(x,y,z);g.add(o);return o;};
 const cyl=(rt,rb,h,m,x,y,z)=>{const o=new THREE.Mesh(new THREE.CylinderGeometry(rt,rb,h,28),m);o.position.set(x,y,z);g.add(o);return o;};
 // Compact board and three clearly separated, correctly connected components.
 box(2.35,.055,1.22,baseMat,0,-.035,0);
 // Cell on the left: raised positive terminal, lower negative terminal.
 cyl(.18,.18,.48,batteryMat,-.82,.26,0);
 cyl(.185,.185,.035,dark,-.82,.505,0);cyl(.065,.065,.07,copper,-.82,.55,0);
 box(.035,.10,.035,metal,-.82,.19,.205);box(.09,.025,.035,metal,-.82,.19,.205);
 box(.09,.025,.035,metal,-.82,.335,.205);
 // Key/switch in the middle, open by default.
 box(.45,.035,.30,material(0x28465e),0,.045,-.40);
 const terminalA=cyl(.055,.055,.075,copper,-.17,.115,-.40);
 const terminalB=cyl(.055,.055,.075,copper,.17,.115,-.40);
 const lever=new THREE.Mesh(new THREE.BoxGeometry(.34,.045,.055),metal);lever.position.set(-.09,.20,-.40);lever.rotation.z=-.18;g.add(lever);
 const pivot=new THREE.Mesh(new THREE.SphereGeometry(.06,18,14),copper);pivot.position.set(-.17,.15,-.40);g.add(pivot);
 // Bulb at right: base, screw contacts and glass globe.
 cyl(.15,.17,.10,dark,.82,.11,0);cyl(.105,.105,.19,metal,.82,.245,0);
 for(let i=0;i<3;i++)cyl(.11,.11,.018,copper,.82,.19+i*.05,0);
 const globe=new THREE.Mesh(new THREE.SphereGeometry(.17,28,24),bulbGlass);globe.position.set(.82,.47,0);g.add(globe);
 tube(g,[[.82,.32,0],[.77,.43,0],[.82,.52,0],[.87,.43,0]],0xd98b45,.012);
 // Closed series path: cell + -> key -> bulb -> cell -.
 tube(g,[[-.82,.55,0],[-.82,.67,-.40],[-.17,.24,-.40]],0xe65d58,.022);
 tube(g,[[.17,.19,-.40],[.48,.23,-.40],[.82,.29,-.22],[.82,.29,0]],0xe65d58,.022);
 tube(g,[[.82,.29,0],[.82,.64,.54],[0,.64,.58],[-.82,.19,.205]],0x4f9be8,.022);
 // Small plain labels printed directly on component surfaces (no callout boxes).
 const componentText=(txt,pos,scale=.16)=>{
  const canvas=document.createElement("canvas");canvas.width=512;canvas.height=128;const ctx=canvas.getContext("2d");
  ctx.clearRect(0,0,512,128);ctx.font="bold 74px Arial";ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillStyle="#f4fbff";ctx.fillText(txt,256,66);
  const tex=new THREE.CanvasTexture(canvas);tex.colorSpace=THREE.SRGBColorSpace;
  const sprite=new THREE.Sprite(new THREE.SpriteMaterial({map:tex,transparent:true,depthTest:true,depthWrite:false}));
  sprite.scale.set(scale,scale*.25,1);sprite.position.set(...pos);sprite.renderOrder=2;g.add(sprite);
 };
 componentText("BATTERY",[-.82,.34,.21],.26);
 componentText("KEY",[0,.14,-.20],.18);
 componentText("BULB",[.82,.43,.18],.20);
 const glow=new THREE.PointLight(0xffc35b,0,.9);glow.position.set(.82,.52,0);g.add(glow);
 g.userData={kind:"circuit",bulbMaterial:bulbGlass,bulbGlow:glow,lever,circuitOn:true};setCircuitState(true,g);
}
function makeMagnetic(g){
 // Horizontal bar magnet with correctly directed closed magnetic field loops.
 const magnet=new THREE.Mesh(new THREE.BoxGeometry(1.5,.34,.38),material(0x263f58,{metalness:.25}));
 g.add(magnet);
 const north=new THREE.Mesh(new THREE.BoxGeometry(.75,.36,.4),material(0xd94e55));north.position.x=-.375;g.add(north);
 const south=new THREE.Mesh(new THREE.BoxGeometry(.75,.36,.4),material(0x397fd0));south.position.x=.375;g.add(south);
 const poleTag=(txt,pos)=>{const t=label(txt);t.scale.set(.28,.17,1);t.position.set(...pos);g.add(t);};
 poleTag("N",[-.38,.02,.23]);poleTag("S",[.38,.02,.23]);
 // Closed loops outside run N to S; inside magnet direction is S to N.
 for(let i=0;i<5;i++){
  const y=.22+i*.12,z=(i-2)*.11,h=.48+i*.13;
  tube(g,[[-.72,y,z],[-.9,h,z],[-.55,h+.16,z],[0,h+.19,z],[.55,h+.16,z],[.9,h,z],[.72,y,z]],0x62d9f2,.009);
 }
 // Arrowheads on the external upper loop show N -> S.
 const arrow=new THREE.Mesh(new THREE.ConeGeometry(.035,.12,12),new THREE.MeshBasicMaterial({color:0x9ceafa}));
 arrow.position.set(.12,.82,0);arrow.rotation.z=-Math.PI/2;g.add(arrow);
}function makeRefraction(g){
 // Parallel-sided glass slab. Ray enters from air, bends toward the normal,
 // exits bending away, and emerges parallel to the incident ray.
 const glassMat=new THREE.MeshPhysicalMaterial({color:0x75c9ef,transparent:true,opacity:.2,roughness:.08,metalness:0,side:THREE.DoubleSide});
 const slab=new THREE.Mesh(new THREE.BoxGeometry(1.18,.9,.42),glassMat);g.add(slab);
 const edges=new THREE.LineSegments(new THREE.EdgesGeometry(slab.geometry),new THREE.LineBasicMaterial({color:0x8fe5ff}));g.add(edges);
 // Entry/exit faces are vertical: their normal is horizontal.
 tube(g,[[-1.22,.55,.28],[-.59,.24,.28]],0xffc95e,.018);
 tube(g,[[-.59,.24,.28],[.59,-.06,.28]],0xffc95e,.018);
 tube(g,[[.59,-.06,.28],[1.22,-.37,.28]],0xffc95e,.018);
 const normal=(x)=>{const line=new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(x,-.56,.32),new THREE.Vector3(x,.56,.32)]),new THREE.LineDashedMaterial({color:0xe7f5ff,dashSize:.06,gapSize:.04}));line.computeLineDistances();g.add(line);};
 normal(-.59);normal(.59);
 const tag=label("GLASS");tag.scale.set(.34,.17,1);tag.position.set(0,-.4,.24);g.add(tag);
}function makeCell(g){
 // Plant cell: rounded outline, cell wall, membrane, nucleus, chloroplasts,
 // large central vacuole, mitochondria and cytoplasm.
 const outer=new THREE.Mesh(new THREE.SphereGeometry(1,40,32),material(0x70b96d,{transparent:true,opacity:.25,side:THREE.DoubleSide}));
 outer.scale.set(1.08,.68,.48);g.add(outer);
 const edge=new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.SphereGeometry(1,32,24)),new THREE.LineBasicMaterial({color:0x83e59a,transparent:true,opacity:.6}));
 edge.scale.set(1.08,.68,.48);g.add(edge);
 const membrane=new THREE.Mesh(new THREE.SphereGeometry(.96,36,28),material(0x63b8a1,{transparent:true,opacity:.13,side:THREE.DoubleSide}));
 membrane.scale.set(1.06,.66,.46);g.add(membrane);
 const cytoplasm=new THREE.Mesh(new THREE.SphereGeometry(.91,32,24),material(0x9bdc85,{transparent:true,opacity:.08,side:THREE.DoubleSide}));
 cytoplasm.scale.set(1.04,.64,.44);g.add(cytoplasm);
 const vac=new THREE.Mesh(new THREE.SphereGeometry(1,32,24),material(0x65b9e8,{transparent:true,opacity:.48}));
 vac.scale.set(.48,.43,.30);vac.position.set(.28,-.02,.03);g.add(vac);
 const nucleus=new THREE.Mesh(new THREE.SphereGeometry(.22,32,24),material(0xb38be8));nucleus.position.set(-.53,.12,.16);g.add(nucleus);
 const nucleolus=new THREE.Mesh(new THREE.SphereGeometry(.08,24,18),material(0x684a9c));nucleolus.position.set(-.50,.12,.25);g.add(nucleolus);
 // Chloroplasts distributed around the cytoplasm (not inside the vacuole).
 const chlorMat=material(0x3fbd73);
 [[-.68,.38,.13],[-.18,.45,.13],[-.70,-.12,.13],[-.20,-.42,.13],[.72,.34,.13],[.72,-.36,.13]].forEach(p=>{
  const c=new THREE.Mesh(new THREE.SphereGeometry(.09,20,16),chlorMat);c.scale.set(1.45,.72,.8);c.position.set(...p);g.add(c);
 });
 // Mitochondria are small elongated bodies with folded inner-membrane hints.
 const mitoMat=material(0xe7a45c);
 [[-.20,.62,.12],[.35,.55,.12],[-.74,.5,.12]].forEach(p=>{
  const m=new THREE.Mesh(new THREE.SphereGeometry(.105,20,14),mitoMat);m.scale.set(1.65,.75,.8);m.position.set(...p);g.add(m);
 });
}function makeModel(kind){const g=new THREE.Group();g.userData.arExperimentRoot=true;if(kind==="atom")makeAtom(g);else if(kind==="circuit")makeCircuit(g);else if(kind==="magnetic")makeMagnetic(g);else if(kind==="refraction")makeRefraction(g);else if(kind==="cell")makeCell(g);return g;}
function setCircuitState(on,target=model){if(!target||target.userData?.kind!=="circuit")return;target.userData.circuitOn=!!on;target.userData.bulbMaterial.emissiveIntensity=on?.95:.035;target.userData.bulbMaterial.emissive.setHex(on?0xffa92e:0x3b2b16);target.userData.bulbGlow.intensity=on?1.8:0;target.userData.lever.rotation.z=on?0:-.48;}
function setup(){if(renderer&&renderer.domElement?.isConnected){stage.querySelectorAll("canvas").forEach((c,i)=>{if(c!==renderer.domElement)c.remove();});return;}stage.querySelectorAll("canvas").forEach(c=>c.remove());renderer=new THREE.WebGLRenderer({alpha:true,antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));renderer.setSize(stage.clientWidth,stage.clientHeight);renderer.xr.enabled=true;renderer.domElement.dataset.arRenderer="primary";stage.appendChild(renderer.domElement);scene=new THREE.Scene();camera3d=new THREE.PerspectiveCamera(55,stage.clientWidth/stage.clientHeight,.01,30);scene.add(new THREE.HemisphereLight(0xffffff,0x34516b,2));const light=new THREE.DirectionalLight(0xffffff,2);light.position.set(1,3,2);scene.add(light);changeModel();renderer.setAnimationLoop(()=>renderer.render(scene,camera3d));window.addEventListener("resize",resize);}
function resize(){if(!renderer)return;renderer.setSize(stage.clientWidth,stage.clientHeight);camera3d.aspect=stage.clientWidth/stage.clientHeight;camera3d.updateProjectionMatrix();}
function changeModel(){if(!scene)return;scene.children.filter(o=>o.userData?.arExperimentRoot||o.name==="active-scientific-model").forEach(o=>{scene.remove(o);o.traverse(n=>{if(n.geometry)n.geometry.dispose();if(n.material)(Array.isArray(n.material)?n.material:[n.material]).forEach(m=>{if(m.map)m.map.dispose();m.dispose();});});});if(model&&model.parent)scene.remove(model);const id=$("#modelSelect").value,d=catalogue[id];model=makeModel(d.kind);model.name="active-scientific-model";scene.add(model);model.position.set(0,0,-2);model.scale.setScalar(.65);$("#modelTitle").textContent=d.title;$("#modelInfo").textContent=d.info;$("#modelMeta").textContent=d.subject+"  •  "+d.grade;$("#modelFacts").innerHTML=d.facts.map(x=>"<li>"+x+"</li>").join("");}
async function startAR(){if(session){status.textContent="An AR session is already running. Exit it before starting another.";return;}setup();if(!navigator.xr){status.textContent="WebXR AR is unavailable in this browser. Try Camera Preview.";return;}try{if(!await navigator.xr.isSessionSupported("immersive-ar")){status.textContent="This device/browser does not support immersive AR. Try Camera Preview.";return;}session=await navigator.xr.requestSession("immersive-ar",{requiredFeatures:["hit-test"],optionalFeatures:["local-floor","dom-overlay"],domOverlay:{root:document.body}});let refType=null;for(const candidate of ["local-floor","local"]){try{await session.requestReferenceSpace(candidate);refType=candidate;break;}catch(_){}}if(!refType)throw new Error("No supported local reference space was found.");renderer.xr.setReferenceSpaceType(refType);await renderer.xr.setSession(session);refSpace=renderer.xr.getReferenceSpace();if(!refSpace)throw new Error("Three.js could not access the active AR reference space.");const viewer=await session.requestReferenceSpace("viewer");hitSource=await session.requestHitTestSource({space:viewer});const reticle=new THREE.Mesh(new THREE.RingGeometry(.08,.11,32),new THREE.MeshBasicMaterial({color:0x70edbd,side:THREE.DoubleSide}));reticle.rotation.x=-Math.PI/2;reticle.matrixAutoUpdate=false;reticle.visible=false;scene.add(reticle);let placed=false;const controller=renderer.xr.getController(0);scene.add(controller);const raycaster=new THREE.Raycaster();controller.addEventListener("select",()=>{if(model?.userData.kind==="circuit"){raycaster.setFromXRController(controller);if(raycaster.intersectObject(model.userData.lever).length){setCircuitState(!model.userData.circuitOn,model);status.textContent=model.userData.circuitOn?"Switch closed: bulb ON.":"Switch open: bulb OFF.";return;}}if(reticle.visible&&!placed){model.position.setFromMatrixPosition(reticle.matrix);model.quaternion.setFromRotationMatrix(reticle.matrix);model.scale.setScalar(.65);placed=true;reticle.visible=false;status.textContent="Model placed once. Move around it to observe different sides.";}});renderer.setAnimationLoop((time,frame)=>{if(frame&&hitSource){const hits=frame.getHitTestResults(hitSource);if(hits.length&&!placed){const pose=hits[0].getPose(refSpace);reticle.visible=true;reticle.matrix.fromArray(pose.transform.matrix);}else reticle.visible=false;}renderer.render(scene,camera3d);});session.addEventListener("end",()=>{session=null;hitSource=null;refSpace=null;reticle.visible=false;scene.remove(reticle);scene.remove(controller);document.body.classList.remove("ar-active");resize();renderer.setAnimationLoop(()=>renderer.render(scene,camera3d));status.textContent="AR session ended.";$("#stopAR").disabled=true;});$("#stopAR").disabled=false;$("#placeModel").disabled=false;$("#rotateModel").disabled=false;hint.hidden=true;document.body.classList.add("ar-active");resize();status.textContent="Move your phone slowly to find a surface. Tap to place the model.";}catch(e){if(session){try{await session.end();}catch(_){}session=null;}hitSource=null;refSpace=null;status.textContent="Could not start true surface AR: "+(e.message||"AR setup failed")+". Camera Preview remains available.";}}
async function startPreview(){setup();previewMode=true;try{previewStream=await navigator.mediaDevices.getUserMedia({video:{facingMode:{ideal:"environment"}},audio:false});camera.srcObject=previewStream;await camera.play();document.body.classList.add("preview-active");camera.style.display="block";stage.style.background="transparent";hint.hidden=true;renderer.setAnimationLoop(()=>renderer.render(scene,camera3d));model.position.set(0,0,-2);status.textContent="Camera preview shows a draggable 3D model overlay; it does not automatically detect surfaces.";$("#placeModel").disabled=false;$("#rotateModel").disabled=false;$("#stopAR").disabled=false;}catch(e){status.textContent="Camera access was not granted. Allow camera permission and reload.";}}
$("#modelSelect").addEventListener("change",changeModel);$("#startAR").addEventListener("click",startAR);$("#cameraMode").addEventListener("click",startPreview);$("#rotateModel").addEventListener("click",()=>{if(model)model.rotation.y+=Math.PI/4;});$("#placeModel").addEventListener("click",()=>{if(model){model.position.set(0,0,-2);model.rotation.set(0,0,0);status.textContent="Model reset to the view."; }});
$("#stopAR").addEventListener("click",async()=>{if(session)await session.end();if(previewStream){previewStream.getTracks().forEach(t=>t.stop());previewStream=null;}camera.style.display="none";document.body.classList.remove("ar-active","preview-active");resize();previewMode=false;$("#stopAR").disabled=true;$("#placeModel").disabled=true;$("#rotateModel").disabled=true;hint.hidden=false;status.textContent="Experience ended.";});
setup();renderer.domElement.style.touchAction="none";renderer.domElement.addEventListener("pointerdown",e=>{if(!previewMode&&!session)return;dragging=true;lastX=e.clientX;lastY=e.clientY;dragStartX=e.clientX;dragStartY=e.clientY;renderer.domElement.setPointerCapture?.(e.pointerId);});renderer.domElement.addEventListener("pointermove",e=>{if(!dragging||!model)return;model.rotation.y+=(e.clientX-lastX)*.009;model.rotation.x+=(e.clientY-lastY)*.006;lastX=e.clientX;lastY=e.clientY;});renderer.domElement.addEventListener("pointerup",e=>{if(dragging&&model?.userData.kind==="circuit"&&Math.hypot(e.clientX-dragStartX,e.clientY-dragStartY)<8&&!session){const r=renderer.domElement.getBoundingClientRect(),p=new THREE.Vector2(((e.clientX-r.left)/r.width)*2-1,-((e.clientY-r.top)/r.height)*2+1),ray=new THREE.Raycaster();ray.setFromCamera(p,camera3d);if(ray.intersectObject(model.userData.lever).length)setCircuitState(!model.userData.circuitOn,model);}dragging=false;});renderer.domElement.addEventListener("pointercancel",()=>dragging=false);