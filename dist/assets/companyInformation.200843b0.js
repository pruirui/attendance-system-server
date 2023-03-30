import{aS as _e,aT as he,d as M,$ as ge,X as fe,a as _,c as $,q as Z,l as h,au as ve,aw as b,av as te,a8 as Ee,aE as ye,bf as O,o as Ce,aC as Fe,y as d,i as o,w as n,e as u,e7 as xe,e0 as be,x as l,e8 as De,h as ae,r as k,bg as Ae,e9 as Be,ea as we,E as ke,a3 as Ie,a9 as Se,t as m,n as N,aa as S,eb as $e,ec as Ve,ed as Ue,ee as ze,p as Te,b as Ne,ef as qe,dX as ee,dY as Me,eg as Pe,dZ as Re,ab as X,ac as je,eh as He,ei as Le,m as Oe,ej as We,_ as Xe}from"./index.9c52b99a.js";import{E as Ge}from"./el-card.bb5ca019.js";import{E as Qe}from"./el-overlay.8c6f0907.js";import{E as Je}from"./el-pagination.18f1876d.js";import{E as Ke}from"./el-input.76522da5.js";/* empty css               */import"./el-select.cb4f0ecd.js";import{E as Ye,a as Ze}from"./el-table-column.5eb4796d.js";import"./el-checkbox.99d107ff.js";import{e as et}from"./util.ed0d6e80.js";import{E as tt}from"./el-row.c2f6deb8.js";import{E as at}from"./el-col.01f399ab.js";import{E as q}from"./index.b0a55544.js";import"./event.caa1cd05.js";import"./scroll.9df58ebe.js";import"./index.921ddcd1.js";import"./index.85908338.js";import"./strings.1531c023.js";import"./validator.a3ba21c6.js";import"./_initCloneObject.8439a0d9.js";import"./flatten.f7ca8560.js";const ut=_e({direction:{type:String,values:["horizontal","vertical"],default:"horizontal"},contentPosition:{type:String,values:["left","center","right"],default:"center"},borderStyle:{type:he(String),default:"solid"}}),ot=M({name:"ElDivider"}),st=M({...ot,props:ut,setup(D){const r=D,c=ge("divider"),e=fe(()=>c.cssVar({"border-style":r.borderStyle}));return(y,V)=>(_(),$("div",{class:Z([h(c).b(),h(c).m(y.direction)]),style:te(h(e)),role:"separator"},[y.$slots.default&&y.direction!=="vertical"?(_(),$("div",{key:0,class:Z([h(c).e("text"),h(c).is(y.contentPosition)])},[ve(y.$slots,"default")],2)):b("v-if",!0)],6))}});var nt=Ee(st,[["__file","/home/runner/work/element-plus/element-plus/packages/components/divider/src/divider.vue"]]);const lt=ye(nt);const it={class:"camera-box",style:{width:"1000px"}},rt=u("div",{style:{"text-align":"center","font-size":"14px","font-weight":"bold","margin-bottom":"10px",width:"400px"}},"\u6444\u50CF\u5934",-1),dt=u("video",{id:"videoCamera",width:"400",height:"320"},null,-1),ct={class:"iCenter"},pt=l("\u6253\u5F00\u6444\u50CF\u5934"),mt=l("\u62CD \u7167"),_t=l("\u5173\u95ED\u6444\u50CF\u5934"),ht=u("div",{style:{"text-align":"center","font-size":"14px","font-weight":"bold","margin-bottom":"10px",width:"400px"}},"\u62CD\u6444\u6548\u679C",-1),gt=u("canvas",{id:"canvasCamera",width:"400",height:"320",style:{display:"block"}},null,-1),ft=l("\u4E0A\u4F20\u4EBA\u8138\u4FE1\u606F"),vt=M({__name:"faceImport",props:["uid"],emits:["changevisible"],setup(D,{emit:r}){const c=D,e=O({open:!1,loading:!1,imgSrc:"",faceFlag:!1,thisCancas:null,thisContext:null,thisVideo:null,videoWidth:400,videoHeight:320});Ce(()=>{V()}),Fe(()=>{y(),e.open=!1,e.loading=!1,e.imgSrc="",e.faceFlag=!1,e.thisCancas=null,e.thisVideo=null,e.thisContext=null});const y=()=>{e.open&&(e.open=!1,e.thisVideo.srcObject.getTracks()[0].stop())},V=()=>{e.thisCancas=document.getElementById("canvasCamera"),e.thisContext=e.thisCancas.getContext("2d"),e.thisVideo=document.getElementById("videoCamera"),e.thisVideo.style.dispaly="block",navigator.mediaDevices===void 0&&(navigator.mediaDevices={}),navigator.mediaDevices.getUserMedia===void 0&&(navigator.mediaDevices.getUserMedia=function(p){var f=navigator.webkitGetUserMedia||navigator.mozGetUserMedia||navigator.getUserMedia;return f?new Promise(function(v,E){f.call(navigator,p,v,E)}):Promise.reject(new Error("getUserMedia is not implemented in this browser"))});var i={audio:!1,video:{width:e.videoWidth,height:e.videoHeight,transform:"scaleX(-1)"}};navigator.mediaDevices.getUserMedia(i).then(function(p){"srcObject"in e.thisVideo?e.thisVideo.srcObject=p:e.thisVideo.src=window.URL.createObjectURL(p),e.thisVideo.onloadedmetadata=function(f){e.thisVideo.play()}}).catch(p=>{d.error("\u8BF7\u5728\u6709\u6444\u50CF\u5934\u7684\u7535\u8111\u4E0A\u5141\u8BB8\u6D4F\u89C8\u5668\u4E2D\u7684\u9690\u79C1\u8BBE\u7F6E\u4F7F\u7528\u6444\u50CF\u5934\uFF0C\u5EFA\u8BAE\u4F7F\u7528IE10\u4EE5\u4E0A\u53CA\u6700\u65B0\u7248\u8C37\u6B4C\u3001QQ\u3001\u706B\u72D0\u7B49\u6E38\u6D4F\u89C8\u5668\u3002")}),e.open=!0},P=()=>{if(e.open){e.thisContext.drawImage(e.thisVideo,0,0,e.videoWidth,e.videoHeight);var i=e.thisCancas.toDataURL("image/png");e.imgSrc=i,e.loading=!0}else d.error("\u8BF7\u6253\u5F00\u6444\u50CF\u5934.")},R=()=>{if(e.imgSrc==="")console.log("null"),q.alert("\u4F60\u6CA1\u6709\u62CD\u7167","Error",{confirmButtonText:"OK",callback:i=>{d({type:"error",message:`action: ${i}`})}});else{let i={headers:{"Content-Type":"multipart/form-data"}};De(g(e.imgSrc,"file.jpg"),c.uid,i).then(p=>{console.log(p),p.data.code===1?(d.success(p.data.msg),e.loading=!0,r("changevisible")):q.alert(p.data.msg,"Error",{center:!0,type:"error"})})}},g=(i,p)=>{for(var f=i.split(","),v=f[0].match(/:(.*?);/)[1],E=atob(f[1]),A=E.length,U=new Uint8Array(A);A--;)U[A]=E.charCodeAt(A);return new File([U],p,{type:v})};return(i,p)=>{const f=ae,v=at,E=tt;return _(),$("div",it,[o(E,{gutter:20},{default:n(()=>[o(v,{span:12},{default:n(()=>[rt,dt,u("div",ct,[o(f,{type:"primary",size:"small",onClick:V,style:{"margin-top":"10px"}},{default:n(()=>[pt]),_:1}),o(f,{type:"primary",size:"small",icon:h(xe),onClick:P,style:{"margin-top":"10px"}},{default:n(()=>[mt]),_:1},8,["icon"]),o(f,{type:"primary",size:"small",onClick:y,style:{"margin-top":"10px"}},{default:n(()=>[_t]),_:1})])]),_:1}),o(v,{span:12},{default:n(()=>[ht,gt,o(f,{icon:h(be),type:"primary",size:"small",onClick:R,style:{"margin-top":"10px"}},{default:n(()=>[ft]),_:1},8,["icon"])]),_:1})]),_:1})])}}}),x=D=>(Te("data-v-ea49187a"),D=D(),Ne(),D),Et={class:"container"},yt={class:"card"},Ct={class:"left"},Ft={class:"right"},xt={class:"card-header"},bt=x(()=>u("div",{style:{width:"auto",height:"0px","border-top":"1px black dashed"}},null,-1)),Dt={class:"text item"},At=x(()=>u("span",null,"\u6CE8\u518C\u4EBA:",-1)),Bt=x(()=>u("span",null,"\u6CE8\u518C\u8D44\u672C:",-1)),wt=x(()=>u("span",null,"\u6CE8\u518C\u65E5\u671F:",-1)),kt={class:"text item"},It=x(()=>u("span",null,"\u56E2\u961F\u7535\u8BDD:",-1)),St={class:"text item"},$t=x(()=>u("span",null,"\u5730\u5740:",-1)),Vt={class:"text item"},Ut=x(()=>u("span",null,"\u90E8\u95E8\u7B80\u4ECB:",-1)),zt={class:"handle-box"},Tt=l("\u641C\u7D22"),Nt=l(" \u6388\u4E88HR\u6743\u9650 "),qt=l(" \u5220\u9664\u5458\u5DE5 "),Mt=l(" \u4EBA\u8138\u5BFC\u5165 "),Pt={class:"pagination"},Rt=l("\u5220\u9664\u56E2\u961F"),jt=l("\u4FEE\u6539\u56E2\u961F\u4FE1\u606F"),Ht=l("\u9080\u8BF7\u5458\u5DE5\u52A0\u5165\u56E2\u961F"),Lt={class:"faceimp"},Ot={class:"dialog-footer"},Wt=l("\u53D6 \u6D88"),Xt=l("\u786E \u5B9A"),Gt={class:"handle-box"},Qt=l("\u641C\u7D22"),Jt={class:"info"},Kt={class:"info-image"},Yt={class:"userright"},Zt={class:"username"},ea={style:{"font-size":"large"}},ta={class:"text2"},aa=x(()=>u("span",null,"\u624B\u673A\u53F7:",-1)),ua=x(()=>u("span",null,"\u90AE\u7BB1:",-1)),oa=x(()=>u("span",null,"\u5730\u5740:",-1)),sa={class:"pagination"},na=M({name:"baseform"}),la=M({...na,setup(D){const r=O({departmentid:"",departmentName:"",username:"",rmb:"",createTime:"",phone:"",address:"",description:""}),c=O({querystring:"",pageIndex:1,pageSize:10}),e=O({querystring:"",pageIndex:1,pageSize:5}),y=k([]),V=k([]),P=k(0),R=k(0),g=localStorage.getItem("ms_userId"),i=localStorage.getItem("departmentId"),p=Ae(),f=Be(),v=we(),E=k(!1),A=k(!1),U=k(),B=k(!0),z=()=>{let s=v.list.length-1;const a=v.list[s];v.delTagsItem(s);const C=v.list[s]?v.list[s]:v.list[s-1];C?a.path===f.fullPath&&p.push(C.path):p.push("/")};g===null&&(d.error("\u672A\u68C0\u6D4B\u5230\u7528\u6237\u767B\u5165\uFF0C\u8BF7\u767B\u5165\uFF01"),localStorage.clear(),p.push("/login")),i===null&&(d.error("\u672A\u68C0\u6D4B\u5230\u90E8\u95E8\uFF01"),z()),(()=>{if(i===null){d.error("\u672A\u68C0\u6D4B\u5230\u90E8\u95E8\uFF01"),z();return}$e(i).then(s=>{if(s.status!=200){d.error("\u51FA\u9519\u4E86");return}let a=s.data;if(a.code==1){if(console.log(a),r.departmentid=a.data.departmentid,r.departmentName=a.data.departmentName,r.username=a.data.username,r.rmb=a.data.rmb,r.createTime=a.data.createTime,r.phone=a.data.phone,r.address=a.data.address,r.description=a.data.description,g==null)return;Ve(r.departmentid,g).then(C=>{C.data.data.flag?B.value=!0:B.value=!1})}else d.error(a.msg)}).catch(s=>{d.error("\u7F51\u8DEF\u8D85\u65F6\uFF01")})})();const j=()=>{if(i===null){d.error("\u672A\u68C0\u6D4B\u5230\u90E8\u95E8\uFF01"),z();return}console.log(c),Ue(i,c.querystring,c.pageIndex,c.pageSize).then(s=>{console.log(s),y.value=s.data.data,P.value=s.data.totals})},H=()=>{console.log(e),qe(e.querystring,e.pageIndex,e.pageSize).then(s=>{console.log(s),V.value=s.data.data,R.value=s.data.totals})};j();const G=(s,a,C)=>{C==1&&q.confirm("\u786E\u5B9A\u8981\u6388\u4E88\u7528\u6237 "+a.username+" HR\u6743\u9650\u5417\uFF1F","\u63D0\u793A",{type:"warning"}).then(()=>{if(i===null||g===null){d.error("\u672A\u68C0\u6D4B\u5230\u90E8\u95E8\u6216\u8005\u65E0\u7528\u6237\uFF01"),z();return}He(g,a.id,i).then(I=>{if(I.status!=200){d.error("\u51FA\u9519\u4E86");return}let L=I.data;d.success(L.msg),j()})}).catch(()=>{}),C==2&&q.confirm("\u786E\u5B9A\u8981\u5220\u9664\u7528\u6237 "+a.username+" \u5417\uFF1F","\u63D0\u793A",{type:"warning"}).then(()=>{if(g===null||i===null)return!1;Le(g,a.id,i).then(I=>{console.log(I),d.success(I.data.msg)})}).catch(()=>{})},ue=()=>{c.pageIndex=1,j()},oe=()=>{c.pageIndex=1,H()},se=s=>{c.pageIndex=s,j()},ne=s=>{e.pageIndex=s,H()},le=()=>{q.confirm("\u786E\u5B9A\u8981\u5220\u9664\u8BE5\u90E8\u95E8\u5417\uFF1F","\u63D0\u793A",{type:"warning"}).then(()=>{if(i===null||g===null){d.error("\u672A\u68C0\u6D4B\u5230\u90E8\u95E8\u6216\u8005\u65E0\u7528\u6237\uFF01"),z();return}ze(i,g).then(s=>{if(s.status!=200){d.error("\u51FA\u9519\u4E86");return}let a=s.data;d.info(a.msg)})}).catch(()=>{})},ie=()=>{i!==null&&(localStorage.setItem("departmentId",i),p.push("/modifycompany"))},re=s=>{U.value=s,E.value=!0},de=s=>{i!==null&&q.confirm("\u786E\u5B9A\u9080\u8BF7\u7528\u6237 "+s.username+" \u5230 "+r.departmentName+" \u5417\uFF1F","\u63D0\u793A",{type:"warning"}).then(()=>{if(i===null||g===null){d.error("\u672A\u68C0\u6D4B\u5230\u90E8\u95E8\u6216\u8005\u65E0\u7528\u6237\uFF01"),z();return}We(g,s.id,i).then(a=>{if(a.status!=200){d.error("\u51FA\u9519\u4E86");return}d.success(a.data.msg),H()})}).catch(()=>{})},ce=()=>{A.value=!0,H()};return(s,a)=>{var Y;const C=ke,I=lt,L=Ke,F=ae,w=Ye,pe=Ze,Q=Ie,J=Je,K=Qe,me=Ge,T=Se("permiss");return _(),$("div",Et,[u("div",yt,[u("div",Ct,[o(C,{class:"avatar",style:te(`background:${h(et)(r.departmentName)}`),shape:"square",size:90},{default:n(()=>[l(m(r.departmentName.substr(0,4)),1)]),_:1},8,["style"])]),u("div",Ft,[u("div",xt,[u("span",null,m(r.departmentName),1)]),bt,u("div",Dt,[At,l(" "+m(r.username)+"\xA0\xA0\xA0\xA0 ",1),Bt,l(m(r.rmb)+"\xA0\xA0\xA0\xA0 ",1),wt,l(m(r.createTime),1)]),u("div",kt,[It,l(m(r.phone),1)]),u("div",St,[$t,l(m(r.address),1)]),u("div",Vt,[Ut,l(m(r.description),1)])])]),o(I),o(Q,{height:"400px"},{default:n(()=>[u("div",zt,[o(L,{modelValue:c.querystring,"onUpdate:modelValue":a[0]||(a[0]=t=>c.querystring=t),placeholder:"\u5458\u5DE5\u540D\u6216\u8005\u5458\u5DE5\u624B\u673A\u53F7",class:"handle-input mr10"},null,8,["modelValue"]),o(F,{type:"primary",icon:h(ee),onClick:ue},{default:n(()=>[Tt]),_:1},8,["icon"])]),o(pe,{data:y.value,border:"",class:"table",ref:"multipleTable","header-cell-class-name":"table-header"},{default:n(()=>[o(w,{prop:"username",label:"\u7528\u6237\u540D"}),o(w,{prop:"phone",label:"\u624B\u673A\u53F7"}),o(w,{prop:"gender",label:"\u6027\u522B",width:"80px"}),o(w,{prop:"email",label:"\u90AE\u7BB1"},{default:n(t=>[l(m(t.row.email?t.row.email:"\u65E0"),1)]),_:1}),o(w,{prop:"birthday",label:"\u751F\u65E5"},{default:n(t=>[l(m(t.row.birthday?t.row.birthday:"\u65E0"),1)]),_:1}),o(w,{prop:"address",label:"\u5730\u5740"},{default:n(t=>[l(m(t.row.address?t.row.address:"\u65E0"),1)]),_:1}),o(w,{prop:"role",label:"\u89D2\u8272",width:"100px"},{default:n(t=>[l(m(t.row.role==="user"?"\u5458\u5DE5":t.row.role==="hr"?"HR":t.row.role),1)]),_:1}),o(w,{label:"\u64CD\u4F5C",width:"220",align:"left"},{default:n(t=>[u("div",null,[B.value?N((_(),S(F,{key:0,text:"",icon:h(Me),onClick:W=>G(t.$index,t.row,1)},{default:n(()=>[Nt]),_:2},1032,["icon","onClick"])),[[T,5]]):b("",!0)]),u("div",null,[B.value?N((_(),S(F,{key:0,text:"",icon:h(Pe),onClick:W=>G(t.$index,t.row,2)},{default:n(()=>[qt]),_:2},1032,["icon","onClick"])),[[T,6]]):b("",!0)]),u("div",null,[B.value?N((_(),S(F,{key:0,text:"",icon:h(Re),onClick:W=>re(t.row)},{default:n(()=>[Mt]),_:2},1032,["icon","onClick"])),[[T,6]]):b("",!0)])]),_:1})]),_:1},8,["data"])]),_:1}),u("div",Pt,[o(J,{background:"",layout:"total, prev, pager, next","current-page":c.pageIndex,"page-size":c.pageSize,total:P.value,"pager-count":6,onCurrentChange:se},null,8,["current-page","page-size","total"])]),B.value?N((_(),S(F,{key:0,type:"primary",onClick:a[1]||(a[1]=t=>le())},{default:n(()=>[Rt]),_:1})),[[T,5]]):b("",!0),B.value?N((_(),S(F,{key:1,type:"primary",onClick:a[2]||(a[2]=t=>ie())},{default:n(()=>[jt]),_:1})),[[T,6]]):b("",!0),B.value?N((_(),S(F,{key:2,type:"primary",onClick:a[3]||(a[3]=t=>ce())},{default:n(()=>[Ht]),_:1})),[[T,6]]):b("",!0),o(K,{title:"\u4E3A\u5458\u5DE5 "+((Y=U.value)==null?void 0:Y.username)+" \u5F55\u5165\u4EBA\u8138",modelValue:E.value,"onUpdate:modelValue":a[6]||(a[6]=t=>E.value=t),width:"1000px","destroy-on-close":""},{footer:n(()=>[u("span",Ot,[o(F,{onClick:a[4]||(a[4]=t=>E.value=!1)},{default:n(()=>[Wt]),_:1}),o(F,{type:"primary",onClick:a[5]||(a[5]=t=>E.value=!1)},{default:n(()=>[Xt]),_:1})])]),default:n(()=>{var t;return[u("div",Lt,[o(vt,{uid:(t=U.value)==null?void 0:t.id},null,8,["uid"])])]}),_:1},8,["title","modelValue"]),o(K,{title:"\u9080\u8BF7\u7528\u6237\u52A0\u5165\u56E2\u961F",modelValue:A.value,"onUpdate:modelValue":a[8]||(a[8]=t=>A.value=t),"destroy-on-close":""},{default:n(()=>[u("div",Gt,[o(L,{modelValue:e.querystring,"onUpdate:modelValue":a[7]||(a[7]=t=>e.querystring=t),placeholder:"\u5458\u5DE5\u540D\u6216\u8005\u5458\u5DE5\u624B\u673A\u53F7",class:"handle-input mr10"},null,8,["modelValue"]),o(F,{type:"primary",icon:h(ee),onClick:oe},{default:n(()=>[Qt]),_:1},8,["icon"])]),o(Q,{height:"400px"},{default:n(()=>[(_(!0),$(X,null,je(V.value,t=>(_(),S(me,{shadow:"hover",class:"usercard",onClick:W=>de(t)},{default:n(()=>[u("div",Jt,[u("div",Kt,[o(C,{size:70,src:h(Oe).baseUrl+t.headshot},null,8,["src"])]),u("div",Yt,[u("div",Zt,[u("span",ea,m(t.username),1)]),u("div",ta,[aa,l(" "+m(t.phone)+"\xA0\xA0\xA0\xA0 ",1),t.email?(_(),$(X,{key:0},[ua,l(m(t.email)+"\xA0\xA0\xA0\xA0 ",1)],64)):b("",!0),t.address?(_(),$(X,{key:1},[oa,l(m(t.address)+"\xA0\xA0\xA0\xA0 ",1)],64)):b("",!0)])])])]),_:2},1032,["onClick"]))),256))]),_:1}),u("div",sa,[o(J,{background:"",layout:"total, prev, pager, next","current-page":e.pageIndex,"page-size":e.pageSize,total:R.value,"pager-count":4,onCurrentChange:ne},null,8,["current-page","page-size","total"])])]),_:1},8,["modelValue"])])}}});const Ia=Xe(la,[["__scopeId","data-v-ea49187a"]]);export{Ia as default};
