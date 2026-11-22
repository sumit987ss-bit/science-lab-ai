function makeAtom(g){
 // Carbon-12: 6 protons, 6 neutrons; electron arrangement 2,4.
 const proton=material(0xe66a70,{emissive:0x5b1018,emissiveIntensity:.12});
 const neutron=material(0x5d9ed6,{emissive:0x102e55,emissiveIntensity:.12});
 const electron=material(0x63e0bd,{emissive:0x145b49,emissiveIntensity:.22});
 const positions=[[0,0,0],[.12,0,.08],[-.12,.08,0],[0,-.12,.08],[.08,.12,-.08],[-.08,-.08,-.1],[.04,-.1,-.12],[-.1,.02,.12],[.12,.1,.02],[0,.12,.12],[-.12,-.1,0],[.1,-.04,-.12]];
 positions.forEach((p,i)=>{const m=new THREE.Mesh(new THREE.SphereGeometry(.105,24,18),i<6?proton:neutron);m.position.set(...p);g.add(m);});
 [.48,.82].forEach((r,i)=>{const ring=new THREE.Mesh(new THREE.SphereGeometry(r,40,28),new THREE.MeshBasicMaterial({color:i?0x65b8f0:0x72dfb3,wireframe:true,transparent:true,opacity:.22}));ring.scale.set(1,1,.72);g.add(ring);});
 [[0,.48,0],[0,-.48,0],[.82,0,0],[-.82,0,0],[0,0,.59],[0,0,-.59]].forEach(p=>{const e=new THREE.Mesh(new THREE.SphereGeometry(.055,20,16),electron);e.position.set(...p);g.add(e);});
 callout(g,"NUCLEUS: 6p⁺ + 6n⁰",[0,.08,.08],[0,1.25,.1],1.55);
 callout(g,"1st SHELL: 2 e⁻",[0,.48,0],[-1.25,.55,.1],1.15);
 callout(g,"2nd SHELL: 4 e⁻",[.82,0,0],[1.28,-.05,.1],1.15);
 callout(g,"PROTON (+)",[-.12,.08,0],[-1.18,-.75,.15],.95);
 callout(g,"NEUTRON (0)",[.12,.1,.02],[1.18,-.75,.15],1.05);
}function makeAtom(g){
 // Requested schematic shell model: 1 proton, 1 neutron, 2 inner electrons, 8 outer electrons.
 const pMat=material(0xe95761,{emissive:0x421014,emissiveIntensity:.12});
 const nMat=material(0x4b91db,{emissive:0x102b51,emissiveIntensity:.12});
 const eMat=material(0x54dfc2,{emissive:0x105546,emissiveIntensity:.16});
 const particle=(tag,mat,r,pos,labelSize)=>{
   const ball=new THREE.Mesh(new THREE.SphereGeometry(r,32,24),mat);ball.position.set(...pos);g.add(ball);
   const textSprite=label(tag);textSprite.scale.set(labelSize,labelSize*.34,1);textSprite.position.set(pos[0],pos[1]+r+.075,pos[2]);g.add(textSprite);
 };
 particle("p+",pMat,.17,[-.18,0,0],.29);particle("n",nMat,.17,[.18,0,0],.27);
 const shell=(radius,color)=>{const ring=new THREE.Mesh(new THREE.TorusGeometry(radius,.012,10,128),new THREE.MeshBasicMaterial({color}));g.add(ring);};
 const inner=.62,outer=1.18;shell(inner,0x86c9ff);shell(outer,0x7ce5ba);
 [[inner,0,0],[-inner,0,0]].forEach(pos=>particle("e-",eMat,.075,pos,.20));
 for(let i=0;i<8;i++){const a=i*Math.PI/4;particle("e-",eMat,.075,[outer*Math.cos(a),outer*Math.sin(a),0],.20);}
}