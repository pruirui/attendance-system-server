import{d as D,bf as V,bg as b,r as x,f as i,a as y,c as I,e as m,i as e,w as s,s as k,x as f,eo as U,y as c,g as q,h as $,p as A,b as N,_ as S}from"./index.9c52b99a.js";import{E as K,a as L}from"./el-form-item.27524c01.js";import{E as R}from"./el-input.76522da5.js";import"./event.caa1cd05.js";import"./_initCloneObject.8439a0d9.js";const z=n=>(A("data-v-17f34427"),n=n(),N(),n),M={class:"register-wrap"},T={class:"ms-register"},Z=z(()=>m("div",{class:"ms-title"},"\u667A\u6167\u8003\u52E4\u7CFB\u7EDF",-1)),j={class:"register-btn"},G=f("\u6CE8\u518C"),H={class:"register-tips"},J=f("\u8FD4\u56DE\u9996\u9875"),O=D({__name:"register",setup(n){const o=V({username:"",phone:"",password:"",passwd:""}),B={username:[{required:!0,message:"\u8BF7\u8F93\u5165\u7528\u6237\u540D",trigger:"blur"},{pattern:/^[\u4e00-\u9fa5a-zA-Z0-9]{1,8}$/,min:1,max:8,transform(a){return a.trim()},message:"\u8BF7\u8F93\u51651\u52308\u4F4D\u4E2D\u6587\u3001\u5B57\u6BCD\u3001\u6570\u5B57\u7684\u7EC4\u5408",trigger:"blur"}],phone:[{required:!0,message:"\u8BF7\u8F93\u5165\u7535\u8BDD\u53F7\u7801",trigger:"blur"},{pattern:/^1[3|4|5|8|9]{1}[0-9]{9}$/,min:2,max:15,message:"\u624B\u673A\u683C\u5F0F\u9519\u8BEF",trigger:"blur"}],password:[{required:!0,message:"\u8BF7\u8F93\u5165\u5BC6\u7801",trigger:"blur"}],passwd:[{required:!0,validator:(a,u,r)=>{u!==o.password?r(new Error("\u5BC6\u7801\u4E0D\u4E00\u81F4\uFF0C\u8BF7\u91CD\u65B0\u8F93\u5165\uFF01")):r()},trigger:"blur"}]},w=b(),_=x(),g=a=>{!a||(console.log("-----"),a.validate(u=>{if(console.log("-------------"),u)U({username:o.username,phone:o.phone,password:o.password}).then(r=>{r.data.code===-1?c.error(r.data.msg):(c.success("\u6CE8\u518C\u6210\u529F"),w.push("/login"))});else return c.error("\u6CE8\u518C\u5931\u8D25"),!1}))};return(a,u)=>{const r=i("User"),l=q,p=R,d=K,C=i("Iphone"),F=i("Lock"),E=$,h=i("router-link"),v=L;return y(),I("div",M,[m("div",T,[Z,e(v,{model:o,rules:B,ref_key:"register",ref:_,"label-width":"0px",class:"ms-content"},{default:s(()=>[e(d,{prop:"username"},{default:s(()=>[e(p,{modelValue:o.username,"onUpdate:modelValue":u[0]||(u[0]=t=>o.username=t),placeholder:"\u8BF7\u8F93\u5165\u7528\u6237\u540D"},{prepend:s(()=>[e(l,null,{default:s(()=>[e(r)]),_:1})]),_:1},8,["modelValue"])]),_:1}),e(d,{prop:"phone"},{default:s(()=>[e(p,{modelValue:o.phone,"onUpdate:modelValue":u[1]||(u[1]=t=>o.phone=t),placeholder:"\u8BF7\u8F93\u5165\u7535\u8BDD\u53F7\u7801"},{prepend:s(()=>[e(l,null,{default:s(()=>[e(C)]),_:1})]),_:1},8,["modelValue"])]),_:1}),e(d,{prop:"password"},{default:s(()=>[e(p,{type:"password",placeholder:"\u8BF7\u8F93\u5165\u5BC6\u7801",modelValue:o.password,"onUpdate:modelValue":u[2]||(u[2]=t=>o.password=t)},{prepend:s(()=>[e(l,null,{default:s(()=>[e(F)]),_:1})]),_:1},8,["modelValue"])]),_:1}),e(d,{prop:"passwd"},{default:s(()=>[e(p,{type:"password",placeholder:"\u8BF7\u518D\u6B21\u8F93\u5165\u5BC6\u7801",modelValue:o.passwd,"onUpdate:modelValue":u[3]||(u[3]=t=>o.passwd=t),onKeyup:u[4]||(u[4]=k(t=>g(_.value),["enter"]))},{prepend:s(()=>[e(l,null,{default:s(()=>[e(F)]),_:1})]),_:1},8,["modelValue"])]),_:1}),m("div",j,[e(E,{type:"primary",onClick:u[5]||(u[5]=t=>g(_.value))},{default:s(()=>[G]),_:1})]),m("li",H,[e(h,{to:"/login"},{default:s(()=>[J]),_:1})])]),_:1},8,["model"])])])}}});const ee=S(O,[["__scopeId","data-v-17f34427"]]);export{ee as default};
