import{d as D,r as k,bg as S,y as l,bv as E,a9 as N,a as u,c as i,ab as g,n as C,aa as F,w as d,l as p,i as f,ac as w,x as a,h as $,e as t,t as n,av as b,E as V,p as z,b as T,_ as q}from"./index.9c52b99a.js";import{E as L}from"./el-empty.39e1d870.js";import{e as M}from"./util.ed0d6e80.js";const c=_=>(z("data-v-6d1bd920"),_=_(),T(),_),R=a("\u521B\u5EFA\u516C\u53F8"),U=a("\u641C\u7D22\u516C\u53F8"),j=["onClick"],G={class:"card"},H={class:"left"},I={class:"right"},J={class:"card-header"},K=c(()=>t("div",{style:{width:"auto",height:"0px","border-top":"1px black dashed"}},null,-1)),O={class:"text item"},P=c(()=>t("span",null,"\u6CE8\u518C\u4EBA:",-1)),Q=c(()=>t("span",null,"\u6CE8\u518C\u8D44\u672C:",-1)),W=c(()=>t("span",null,"\u6CE8\u518C\u65E5\u671F:",-1)),X={class:"text item"},Y=c(()=>t("span",null,"\u516C\u53F8\u7535\u8BDD:",-1)),Z={class:"text item"},ee=c(()=>t("span",null,"\u5730\u5740:",-1)),te={class:"text item"},se=c(()=>t("span",null,"\u90E8\u95E8\u7B80\u4ECB:",-1)),ae=a("\u521B\u5EFA\u56E2\u961F"),oe=a("\u641C\u7D22\u56E2\u961F"),ue=D({__name:"company",setup(_){let m=localStorage.getItem("ms_userId");const h=k([]),r=S();(()=>{m===null?(l.error("\u672A\u68C0\u6D4B\u5230\u7528\u6237\u767B\u5165\uFF0C\u8BF7\u767B\u5165\uFF01"),localStorage.clear(),r.push("/login")):E(m).then(o=>{if(o.status!=200){l.error("\u51FA\u9519\u4E86");return}let e=o.data;console.log(e),e.code==1?h.value=e.data:l.error(e.msg)})})(),m===null?(l.error("\u672A\u68C0\u6D4B\u5230\u7528\u6237\u767B\u5165\uFF0C\u8BF7\u767B\u5165\uFF01"),localStorage.clear(),r.push("/login")):E(m).then(o=>{if(console.log(o),o.status!=200){l.error("\u51FA\u9519\u4E86");return}let e=o.data;console.log(e),e.code==1?h.value=e.data:l.error(e.msg)}).catch(o=>{l.error("\u7F51\u7EDC\u8D85\u65F6\u4E86")});const x=o=>{localStorage.setItem("departmentId",o),r.push("/companyinformation")};return(o,e)=>{const v=$,B=L,A=V,y=N("permiss");return u(),i("div",null,[h.value.length===0?(u(),i(g,{key:0},[C((u(),F(v,{type:"primary",onClick:e[0]||(e[0]=s=>p(r).push("/createcompany"))},{default:d(()=>[R]),_:1})),[[y,0]]),C((u(),F(v,{type:"primary",onClick:e[1]||(e[1]=s=>p(r).push("/companysearch"))},{default:d(()=>[U]),_:1})),[[y,1]]),f(B,{style:{"align-self":"center"},description:"\u8FD8\u672A\u52A0\u5165\u516C\u53F8\u5462\uFF01"})],64)):(u(),i(g,{key:1},[(u(!0),i(g,null,w(h.value,s=>(u(),i("div",{class:"container",onClick:re=>x(s.departmentid)},[t("div",G,[t("div",H,[f(A,{class:"avatar",style:b(`background:${p(M)(s.departmentName)}`),shape:"square",size:90},{default:d(()=>[a(n(s.departmentName.substr(0,4)),1)]),_:2},1032,["style"])]),t("div",I,[t("div",J,[t("span",null,n(s.departmentName),1)]),K,t("div",O,[P,a(" "+n(s.username)+"\xA0\xA0\xA0\xA0 ",1),Q,a(n(s.rmb)+"\xA0\xA0\xA0\xA0 ",1),W,a(n(s.createTime.split(" ")[0]),1)]),t("div",X,[Y,a(n(s.phone),1)]),t("div",Z,[ee,a(n(s.address),1)]),t("div",te,[se,a(n(s.description),1)])])])],8,j))),256)),C((u(),F(v,{type:"primary",onClick:e[2]||(e[2]=s=>p(r).push("/createcompany"))},{default:d(()=>[ae]),_:1})),[[y,0]]),C((u(),F(v,{type:"primary",onClick:e[3]||(e[3]=s=>p(r).push("/companysearch"))},{default:d(()=>[oe]),_:1})),[[y,1]])],64))])}}});const de=q(ue,[["__scopeId","data-v-6d1bd920"]]);export{de as default};
