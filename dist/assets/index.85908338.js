import{aS as w,bz as T,d as v,aq as N,$,X as M,a as n,c as V,e as t,au as m,q as o,l as a,aa as c,w as i,i as g,ba as k,bK as b,g as C,aw as y,av as h,bS as q,a8 as I,aE as P}from"./index.9c52b99a.js";const F=w({closable:Boolean,type:{type:String,values:["success","info","warning","danger",""],default:""},hit:Boolean,disableTransitions:Boolean,color:{type:String,default:""},size:{type:String,values:T,default:""},effect:{type:String,values:["dark","light","plain"],default:"light"},round:Boolean}),K={close:l=>l instanceof MouseEvent,click:l=>l instanceof MouseEvent},X=v({name:"ElTag"}),j=v({...X,props:F,emits:K,setup(l,{emit:r}){const S=l,E=N(),s=$("tag"),u=M(()=>{const{type:e,hit:f,effect:_,closable:z,round:B}=S;return[s.b(),s.is("closable",z),s.m(e),s.m(E.value),s.m(_),s.is("hit",f),s.is("round",B)]}),p=e=>{r("close",e)},d=e=>{r("click",e)};return(e,f)=>e.disableTransitions?(n(),V("span",{key:0,class:o(a(u)),style:h({backgroundColor:e.color}),onClick:d},[t("span",{class:o(a(s).e("content"))},[m(e.$slots,"default")],2),e.closable?(n(),c(a(C),{key:0,class:o(a(s).e("close")),onClick:b(p,["stop"])},{default:i(()=>[g(a(k))]),_:1},8,["class","onClick"])):y("v-if",!0)],6)):(n(),c(q,{key:1,name:`${a(s).namespace.value}-zoom-in-center`,appear:""},{default:i(()=>[t("span",{class:o(a(u)),style:h({backgroundColor:e.color}),onClick:d},[t("span",{class:o(a(s).e("content"))},[m(e.$slots,"default")],2),e.closable?(n(),c(a(C),{key:0,class:o(a(s).e("close")),onClick:b(p,["stop"])},{default:i(()=>[g(a(k))]),_:1},8,["class","onClick"])):y("v-if",!0)],6)]),_:3},8,["name"]))}});var A=I(j,[["__file","/home/runner/work/element-plus/element-plus/packages/components/tag/src/tag.vue"]]);const G=P(A);export{G as E,F as t};