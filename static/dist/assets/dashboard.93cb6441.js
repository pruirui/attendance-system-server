import{d as w,o as N,_ as B,a as k,c as I,p as $,b as D,e as t,r as A,u as P,E as q,f as b,g as R,h as W,i as e,w as s,j as G,k as F,l as h,m as H,t as _,n as K,v as O,q as J,s as Q,x as X,y as Y,z as Z,A as tt}from"./index.9c52b99a.js";import{E as et,a as st}from"./el-table-column.5eb4796d.js";import{E as ot}from"./el-checkbox.99d107ff.js";/* empty css               */import{E as at}from"./el-row.c2f6deb8.js";import{E as nt}from"./el-col.01f399ab.js";import{E as ut}from"./el-card.bb5ca019.js";import"./event.caa1cd05.js";import"./_initCloneObject.8439a0d9.js";import"./flatten.f7ca8560.js";import"./index.921ddcd1.js";window.WIDGET={CONFIG:{layout:"1",width:"400",height:"170",background:"4",dataColor:"000000",backgroundColor:"FFFFFF",language:"zh",aqiColor:"000000",key:"5795d36cae334aac835d35944e564d04"}};const lt=w({setup(){N(()=>{n()});const n=()=>{const l=document.createElement("script");l.type="text/javascript",l.src="https://widget.qweather.net/standard/static/js/he-standard-common.js?v=2.0",document.body.appendChild(l)};return{}}}),dt=n=>($("data-v-5f48eee3"),n=n(),D(),n),ct={class:"weather"},it=dt(()=>t("div",{id:"he-plugin-standard"},null,-1)),rt=[it];function _t(n,l,d,m,x,v){return k(),I("div",ct,rt)}const ht=B(lt,[["render",_t],["__scopeId","data-v-5f48eee3"]]),g=n=>($("data-v-98e7b32c"),n=n(),D(),n),pt={class:"user-info"},ft={class:"user-info-cont"},gt={class:"user-info-name"},mt={class:"user-info-list"},vt={style:{"margin-left":"0px"}},Et={class:"user-info-list"},bt={style:{"margin-left":"0px"}},Ft=g(()=>t("div",{class:"clearfix"},[t("span",null,"\u5929\u6C14\u8BE6\u60C5")],-1)),wt={class:"grid-content grid-con-1"},xt={class:"grid-cont-right"},yt={class:"grid-num"},Ct=g(()=>t("div",null,"\u5165\u804C\u65F6\u957F",-1)),At={class:"grid-content grid-con-2"},Bt={class:"grid-cont-right"},kt={class:"grid-num"},It=g(()=>t("div",null,"\u6253\u5361\u6B21\u6570",-1)),$t={class:"grid-content grid-con-3"},Dt={class:"grid-cont-right"},St={class:"grid-num"},Vt=g(()=>t("div",null,"\u7F3A\u5361\u6B21\u6570",-1)),Tt={class:"clearfix"},Ut=g(()=>t("span",null,"\u5F85\u529E\u4E8B\u9879",-1)),jt=X("\u6DFB\u52A0"),zt=["onUpdate:modelValue","onBlur"],Lt=w({name:"dashboard"}),Mt=w({...Lt,setup(n){const l=A({indate:"100",clock:"100",noclock:"100"}),d=P();d.fresh();const m=localStorage.getItem("ms_role"),x=m==="boss"?"boss":m==="HR"?"HR":m==="admin"?"\u7BA1\u7406\u5458":"\u666E\u901A\u7528\u6237",v=o=>{if(o.content==""||o.content==null){o.status=!1,Y.warning("\u8BF7\u8F93\u5165\u4EE3\u8868\u4E8B\u9879");return}if(console.log("========="),console.log(o),o.id==""){let a=d.user.id;if(a==null)return;Z(a,o.content,o.status).then(p=>{a!=null&&F(a).then(c=>{c.status==200&&(u.value=c.data.data,u.value==null&&(u.value=[]))})})}else tt(o.id,o.content,o.status).then(a=>{d.user.id!=null&&F(d.user.id).then(p=>{p.status==200&&(u.value=p.data.data,u.value==null&&(u.value=[]))})})},S=o=>{o.target.blur()};(()=>{const o=localStorage.getItem("ms_userId");o!==null&&(G(o).then(a=>{l.value=a.data.data}),F(o).then(a=>{console.log("--------"),console.log(a),a.status==200&&(u.value=a.data.data,u.value==null&&(u.value=[]))}))})();const u=A([{id:"",content:"\u4ECA\u5929\u8981\u4FEE\u590D100\u4E2Abug",status:!1},{id:"",content:"\u4ECA\u5929\u8981\u4FEE\u590D100\u4E2Abug",status:!1},{id:"",content:"\u4ECA\u5929\u8981\u5199100\u884C\u4EE3\u7801\u52A0\u51E0\u4E2Abug\u5427",status:!1},{id:"",content:"\u4ECA\u5929\u8981\u4FEE\u590D100\u4E2Abug",status:!1},{id:"",content:"\u4ECA\u5929\u8981\u4FEE\u590D100\u4E2Abug",status:!0}]),V=()=>{u.value.unshift({content:"",status:!1,id:""})};return(o,a)=>{const p=q,c=ut,f=nt,T=b("User"),E=R,U=b("SuccessFilled"),j=b("WarningFilled"),y=at,z=W,L=ot,C=et,M=st;return k(),I("div",null,[e(y,{gutter:20},{default:s(()=>[e(f,{span:8},{default:s(()=>[e(c,{shadow:"hover",class:"mgb20",style:{height:"252px"}},{default:s(()=>[t("div",pt,[e(p,{size:120,src:h(H).baseUrl+h(d).user.headshot},null,8,["src"]),t("div",ft,[t("div",gt,_(h(d).user.username),1),t("div",null,_(h(x)),1)])]),t("div",mt,[t("span",vt,"\u624B\u673A\u53F7\uFF1A"+_(h(d).user.phone),1)]),t("div",Et,[t("span",bt,"\u4E2A\u6027\u7B7E\u540D\uFF1A"+_(h(d).user.motto),1)])]),_:1}),e(c,{shadow:"hover",style:{height:"252px"}},{header:s(()=>[Ft]),default:s(()=>[t("div",null,[e(ht,{class:"weather"})])]),_:1})]),_:1}),e(f,{span:16},{default:s(()=>[e(y,{gutter:20,class:"mgb20"},{default:s(()=>[e(f,{span:8},{default:s(()=>[e(c,{shadow:"hover","body-style":{padding:"0px"}},{default:s(()=>[t("div",wt,[e(E,{class:"grid-con-icon"},{default:s(()=>[e(T)]),_:1}),t("div",xt,[t("div",yt,_(l.value.indate),1),Ct])])]),_:1})]),_:1}),e(f,{span:8},{default:s(()=>[e(c,{shadow:"hover","body-style":{padding:"0px"}},{default:s(()=>[t("div",At,[e(E,{class:"grid-con-icon"},{default:s(()=>[e(U)]),_:1}),t("div",Bt,[t("div",kt,_(l.value.clock),1),It])])]),_:1})]),_:1}),e(f,{span:8},{default:s(()=>[e(c,{shadow:"hover","body-style":{padding:"0px"}},{default:s(()=>[t("div",$t,[e(E,{class:"grid-con-icon"},{default:s(()=>[e(j)]),_:1}),t("div",Dt,[t("div",St,_(l.value.noclock),1),Vt])])]),_:1})]),_:1})]),_:1}),e(c,{shadow:"hover",style:{height:"403px"}},{header:s(()=>[t("div",Tt,[Ut,e(z,{style:{float:"right",padding:"3px 0"},text:"",onClick:V},{default:s(()=>[jt]),_:1})])]),default:s(()=>[e(M,{"show-header":!1,data:u.value,style:{width:"100%",height:"320px"}},{default:s(()=>[e(C,{width:"40"},{default:s(i=>[e(L,{modelValue:i.row.status,"onUpdate:modelValue":r=>i.row.status=r,onChange:r=>v(i.row)},null,8,["modelValue","onUpdate:modelValue","onChange"])]),_:1}),e(C,null,{default:s(i=>[K(t("input",{"onUpdate:modelValue":r=>i.row.content=r,class:J(["todo-item",{"todo-item-del":i.row.status}]),onBlur:r=>v(i.row),onKeyup:a[0]||(a[0]=Q(r=>S(r),["enter"]))},null,42,zt),[[O,i.row.content]])]),_:1})]),_:1},8,["data"])]),_:1})]),_:1})]),_:1})])}}});const Yt=B(Mt,[["__scopeId","data-v-98e7b32c"]]);export{Yt as default};