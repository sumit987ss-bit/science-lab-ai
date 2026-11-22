function makeAtom(g){
 // Requested teaching shell model: 1 proton, 1 neutron, 2 inner electrons, 8 outer electrons.
 // Schematic only; this particle count is not a named neutral element.
 const pMat=material(0xe95761,{emissive:0x421014,emissiveIntensity:.12});
 const nMat=material(0x4b91db,{emissive:0x102b51,emissiveIntensity:.12});
 const eMat=material(0x54dfc2,{emissive:0x105546,emissiveIntensity:.16});
 const makeParticle=(text,mat,r,pos,labelScale=.26)=>{
   const ball=new THREE.Mesh(new THREE.SphereGeometry(r,32,24),mat);
   ball.position.set(...pos);g.add(ball);
   const tag=label(text);tag.scale.set(labelScale,labelScale*.34,1);tag.position.set(pos[0],pos[1]+r+.07,pos[2]);g.add(tag);
   return ball;
 };
 // Central nucleus: exactly one proton and one neutron, close but distinct.
 makeParticle("p+",pMat,.18,[-.19,0,0],.34);
 makeParticle("n",nMat,.18,[.19,0,0],.30);
 // Two separate concentric energy-shell circles in the XY plane; neither intersects the other.
 const shell=(radius,color)=>{
   const ring=new THREE.Mesh(new THREE.TorusGeometry(radius,.012,10,128),new THREE.MeshBasicMaterial({color}));
   ring.rotation.x=0;ring.rotation.y=0;g.add(ring);
 };
 const r1=.62,r2=1.18;
 shell(r1,0x86c9ff);shell(r2,0x7ce5ba);
 // Inner shell: two electrons at opposite positions.
 [[r1,0,0],[-r1,0,0]].forEach(pos=>makeParticle("e-",eMat,.075,pos,.22));
 // Second shell: eight electrons spaced evenly at 45-degree intervals.
 for(let i=0;i<8;i++){
   const a=(i*Math.PI/4)+Math.PI/8;
   makeParticle("e-",eMat,.075,[r2*Math.cos(a),r2*Math.sin(a),0],.22);
 }
}