import{a2 as Ee,X as c,bD as Ae,W as De,r as V,as as ge,aS as Oe,ar as Ke,aT as Z,by as xe,aU as He,aD as Q,d as ke,bE as je,aP as We,aL as Ue,aO as Xe,aq as Ye,aK as qe,$ as we,b4 as ee,bF as Ge,bG as Je,bH as Ze,bt as Qe,ap as et,Y as te,o as tt,a0 as _,bI as at,n as ot,ax as nt,a as p,c as g,aw as v,ab as ae,q as h,l as t,au as H,e as P,aa as w,w as B,aR as j,g as L,bq as oe,i as st,bJ as lt,bK as rt,bL as it,t as W,av as ut,a8 as ct,V as Se,aM as Ce,aE as dt}from"./index.9c52b99a.js";import{U as ne}from"./event.caa1cd05.js";const pt=()=>Ee&&/firefox/i.test(window.navigator.userAgent),ft=o=>/([(\uAC00-\uD7AF)|(\u3130-\u318F)])+/gi.test(o),vt=["class","style"],mt=/^on[A-Z]/,ht=(o={})=>{const{excludeListeners:m=!1,excludeKeys:s}=o,a=c(()=>((s==null?void 0:s.value)||[]).concat(vt)),l=De();return l?c(()=>{var r;return Ae(Object.entries((r=l.proxy)==null?void 0:r.$attrs).filter(([u])=>!a.value.includes(u)&&!(m&&mt.test(u))))}):c(()=>({}))};function yt(o){const m=V();function s(){if(o.value==null)return;const{selectionStart:l,selectionEnd:r,value:u}=o.value;if(l==null||r==null)return;const x=u.slice(0,Math.max(0,l)),d=u.slice(Math.max(0,r));m.value={selectionStart:l,selectionEnd:r,value:u,beforeTxt:x,afterTxt:d}}function a(){if(o.value==null||m.value==null)return;const{value:l}=o.value,{beforeTxt:r,afterTxt:u,selectionStart:x}=m.value;if(r==null||u==null||x==null)return;let d=l.length;if(l.endsWith(u))d=l.length-u.length;else if(l.startsWith(r))d=r.length;else{const y=r[x-1],S=l.indexOf(y,x-1);S!==-1&&(d=S+1)}o.value.setSelectionRange(d,d)}return[s,a]}let b;const bt=`
  height:0 !important;
  visibility:hidden !important;
  ${pt()?"":"overflow:hidden !important;"}
  position:absolute !important;
  z-index:-1000 !important;
  top:0 !important;
  right:0 !important;
`,gt=["letter-spacing","line-height","padding-top","padding-bottom","font-family","font-weight","font-size","text-rendering","text-transform","width","text-indent","padding-left","padding-right","border-width","box-sizing"];function xt(o){const m=window.getComputedStyle(o),s=m.getPropertyValue("box-sizing"),a=Number.parseFloat(m.getPropertyValue("padding-bottom"))+Number.parseFloat(m.getPropertyValue("padding-top")),l=Number.parseFloat(m.getPropertyValue("border-bottom-width"))+Number.parseFloat(m.getPropertyValue("border-top-width"));return{contextStyle:gt.map(u=>`${u}:${m.getPropertyValue(u)}`).join(";"),paddingSize:a,borderSize:l,boxSizing:s}}function Ie(o,m=1,s){var a;b||(b=document.createElement("textarea"),document.body.appendChild(b));const{paddingSize:l,borderSize:r,boxSizing:u,contextStyle:x}=xt(o);b.setAttribute("style",`${x};${bt}`),b.value=o.value||o.placeholder||"";let d=b.scrollHeight;const y={};u==="border-box"?d=d+r:u==="content-box"&&(d=d-l),b.value="";const S=b.scrollHeight-l;if(ge(m)){let f=S*m;u==="border-box"&&(f=f+l+r),d=Math.max(f,d),y.minHeight=`${f}px`}if(ge(s)){let f=S*s;u==="border-box"&&(f=f+l+r),d=Math.min(f,d)}return y.height=`${d}px`,(a=b.parentNode)==null||a.removeChild(b),b=void 0,y}const wt=Oe({id:{type:String,default:void 0},size:Ke,disabled:Boolean,modelValue:{type:Z([String,Number,Object]),default:""},type:{type:String,default:"text"},resize:{type:String,values:["none","both","horizontal","vertical"]},autosize:{type:Z([Boolean,Object]),default:!1},autocomplete:{type:String,default:"off"},formatter:{type:Function},parser:{type:Function},placeholder:{type:String},form:{type:String},readonly:{type:Boolean,default:!1},clearable:{type:Boolean,default:!1},showPassword:{type:Boolean,default:!1},showWordLimit:{type:Boolean,default:!1},suffixIcon:{type:xe},prefixIcon:{type:xe},containerRole:{type:String,default:void 0},label:{type:String,default:void 0},tabindex:{type:[String,Number],default:0},validateEvent:{type:Boolean,default:!0},inputStyle:{type:Z([Object,Array,String]),default:()=>He({})}}),St={[ne]:o=>Q(o),input:o=>Q(o),change:o=>Q(o),focus:o=>o instanceof FocusEvent,blur:o=>o instanceof FocusEvent,clear:()=>!0,mouseleave:o=>o instanceof MouseEvent,mouseenter:o=>o instanceof MouseEvent,keydown:o=>o instanceof Event,compositionstart:o=>o instanceof CompositionEvent,compositionupdate:o=>o instanceof CompositionEvent,compositionend:o=>o instanceof CompositionEvent},Ct=["role"],It=["id","type","disabled","formatter","parser","readonly","autocomplete","tabindex","aria-label","placeholder","form"],Et=["id","tabindex","disabled","readonly","autocomplete","aria-label","placeholder","form"],kt=ke({name:"ElInput",inheritAttrs:!1}),zt=ke({...kt,props:wt,emits:St,setup(o,{expose:m,emit:s}){const a=o,l=je(),r=We(),u=c(()=>{const e={};return a.containerRole==="combobox"&&(e["aria-haspopup"]=l["aria-haspopup"],e["aria-owns"]=l["aria-owns"],e["aria-expanded"]=l["aria-expanded"]),e}),x=c(()=>[a.type==="textarea"?le.b():n.b(),n.m(ze.value),n.is("disabled",k.value),n.is("exceed",Fe.value),{[n.b("group")]:r.prepend||r.append,[n.bm("group","append")]:r.append,[n.bm("group","prepend")]:r.prepend,[n.m("prefix")]:r.prefix||a.prefixIcon,[n.m("suffix")]:r.suffix||a.suffixIcon||a.clearable||a.showPassword,[n.bm("suffix","password-clear")]:D.value&&Y.value},l.class]),d=c(()=>[n.e("wrapper"),n.is("focus",F.value)]),y=ht({excludeKeys:c(()=>Object.keys(u.value))}),{form:S,formItem:f}=Ue(),{inputId:se}=Xe(a,{formItemContext:f}),ze=Ye(),k=qe(),n=we("input"),le=we("textarea"),R=ee(),I=ee(),F=V(!1),U=V(!1),N=V(!1),A=V(!1),re=V(),X=ee(a.inputStyle),T=c(()=>R.value||I.value),ie=c(()=>{var e;return(e=S==null?void 0:S.statusIcon)!=null?e:!1}),$=c(()=>(f==null?void 0:f.validateState)||""),ue=c(()=>$.value&&Ge[$.value]),Pe=c(()=>A.value?Je:Ze),Ve=c(()=>[l.style,a.inputStyle]),ce=c(()=>[a.inputStyle,X.value,{resize:a.resize}]),C=c(()=>Qe(a.modelValue)?"":String(a.modelValue)),D=c(()=>a.clearable&&!k.value&&!a.readonly&&!!C.value&&(F.value||U.value)),Y=c(()=>a.showPassword&&!k.value&&!a.readonly&&!!C.value&&(!!C.value||F.value)),z=c(()=>a.showWordLimit&&!!y.value.maxlength&&(a.type==="text"||a.type==="textarea")&&!k.value&&!a.readonly&&!a.showPassword),q=c(()=>C.value.length),Fe=c(()=>!!z.value&&q.value>Number(y.value.maxlength)),Ne=c(()=>!!r.suffix||!!a.suffixIcon||D.value||a.showPassword||z.value||!!$.value&&ie.value),[Te,$e]=yt(R);et(I,e=>{if(!z.value||a.resize!=="both")return;const i=e[0],{width:E}=i.contentRect;re.value={right:`calc(100% - ${E+15+6}px)`}});const O=()=>{const{type:e,autosize:i}=a;if(!(!Ee||e!=="textarea"||!I.value))if(i){const E=Se(i)?i.minRows:void 0,J=Se(i)?i.maxRows:void 0;X.value={...Ie(I.value,E,J)}}else X.value={minHeight:Ie(I.value).minHeight}},M=()=>{const e=T.value;!e||e.value===C.value||(e.value=C.value)},G=async e=>{Te();let{value:i}=e.target;if(a.formatter&&(i=a.parser?a.parser(i):i,i=a.formatter(i)),!N.value){if(i===C.value){M();return}s(ne,i),s("input",i),await _(),M(),$e()}},de=e=>{s("change",e.target.value)},pe=e=>{s("compositionstart",e),N.value=!0},fe=e=>{var i;s("compositionupdate",e);const E=(i=e.target)==null?void 0:i.value,J=E[E.length-1]||"";N.value=!ft(J)},ve=e=>{s("compositionend",e),N.value&&(N.value=!1,G(e))},Me=()=>{A.value=!A.value,K()},K=async()=>{var e;await _(),(e=T.value)==null||e.focus()},_e=()=>{var e;return(e=T.value)==null?void 0:e.blur()},me=e=>{F.value=!0,s("focus",e)},he=e=>{var i;F.value=!1,s("blur",e),a.validateEvent&&((i=f==null?void 0:f.validate)==null||i.call(f,"blur").catch(E=>Ce()))},Be=e=>{U.value=!1,s("mouseleave",e)},Le=e=>{U.value=!0,s("mouseenter",e)},ye=e=>{s("keydown",e)},Re=()=>{var e;(e=T.value)==null||e.select()},be=()=>{s(ne,""),s("change",""),s("clear"),s("input","")};return te(()=>a.modelValue,()=>{var e;_(()=>O()),a.validateEvent&&((e=f==null?void 0:f.validate)==null||e.call(f,"change").catch(i=>Ce()))}),te(C,()=>M()),te(()=>a.type,async()=>{await _(),M(),O()}),tt(()=>{!a.formatter&&a.parser,M(),_(O)}),m({input:R,textarea:I,ref:T,textareaStyle:ce,autosize:at(a,"autosize"),focus:K,blur:_e,select:Re,clear:be,resizeTextarea:O}),(e,i)=>ot((p(),g("div",oe(t(u),{class:t(x),style:t(Ve),role:e.containerRole,onMouseenter:Le,onMouseleave:Be}),[v(" input "),e.type!=="textarea"?(p(),g(ae,{key:0},[v(" prepend slot "),e.$slots.prepend?(p(),g("div",{key:0,class:h(t(n).be("group","prepend"))},[H(e.$slots,"prepend")],2)):v("v-if",!0),P("div",{class:h(t(d))},[v(" prefix slot "),e.$slots.prefix||e.prefixIcon?(p(),g("span",{key:0,class:h(t(n).e("prefix"))},[P("span",{class:h(t(n).e("prefix-inner")),onClick:K},[H(e.$slots,"prefix"),e.prefixIcon?(p(),w(t(L),{key:0,class:h(t(n).e("icon"))},{default:B(()=>[(p(),w(j(e.prefixIcon)))]),_:1},8,["class"])):v("v-if",!0)],2)],2)):v("v-if",!0),P("input",oe({id:t(se),ref_key:"input",ref:R,class:t(n).e("inner")},t(y),{type:e.showPassword?A.value?"text":"password":e.type,disabled:t(k),formatter:e.formatter,parser:e.parser,readonly:e.readonly,autocomplete:e.autocomplete,tabindex:e.tabindex,"aria-label":e.label,placeholder:e.placeholder,style:e.inputStyle,form:a.form,onCompositionstart:pe,onCompositionupdate:fe,onCompositionend:ve,onInput:G,onFocus:me,onBlur:he,onChange:de,onKeydown:ye}),null,16,It),v(" suffix slot "),t(Ne)?(p(),g("span",{key:1,class:h(t(n).e("suffix"))},[P("span",{class:h(t(n).e("suffix-inner")),onClick:K},[!t(D)||!t(Y)||!t(z)?(p(),g(ae,{key:0},[H(e.$slots,"suffix"),e.suffixIcon?(p(),w(t(L),{key:0,class:h(t(n).e("icon"))},{default:B(()=>[(p(),w(j(e.suffixIcon)))]),_:1},8,["class"])):v("v-if",!0)],64)):v("v-if",!0),t(D)?(p(),w(t(L),{key:1,class:h([t(n).e("icon"),t(n).e("clear")]),onMousedown:rt(t(it),["prevent"]),onClick:be},{default:B(()=>[st(t(lt))]),_:1},8,["class","onMousedown"])):v("v-if",!0),t(Y)?(p(),w(t(L),{key:2,class:h([t(n).e("icon"),t(n).e("password")]),onClick:Me},{default:B(()=>[(p(),w(j(t(Pe))))]),_:1},8,["class"])):v("v-if",!0),t(z)?(p(),g("span",{key:3,class:h(t(n).e("count"))},[P("span",{class:h(t(n).e("count-inner"))},W(t(q))+" / "+W(t(y).maxlength),3)],2)):v("v-if",!0),t($)&&t(ue)&&t(ie)?(p(),w(t(L),{key:4,class:h([t(n).e("icon"),t(n).e("validateIcon"),t(n).is("loading",t($)==="validating")])},{default:B(()=>[(p(),w(j(t(ue))))]),_:1},8,["class"])):v("v-if",!0)],2)],2)):v("v-if",!0)],2),v(" append slot "),e.$slots.append?(p(),g("div",{key:1,class:h(t(n).be("group","append"))},[H(e.$slots,"append")],2)):v("v-if",!0)],64)):(p(),g(ae,{key:1},[v(" textarea "),P("textarea",oe({id:t(se),ref_key:"textarea",ref:I,class:t(le).e("inner")},t(y),{tabindex:e.tabindex,disabled:t(k),readonly:e.readonly,autocomplete:e.autocomplete,style:t(ce),"aria-label":e.label,placeholder:e.placeholder,form:a.form,onCompositionstart:pe,onCompositionupdate:fe,onCompositionend:ve,onInput:G,onFocus:me,onBlur:he,onChange:de,onKeydown:ye}),null,16,Et),t(z)?(p(),g("span",{key:0,style:ut(re.value),class:h(t(n).e("count"))},W(t(q))+" / "+W(t(y).maxlength),7)):v("v-if",!0)],64))],16,Ct)),[[nt,e.type!=="hidden"]])}});var Pt=ct(zt,[["__file","/home/runner/work/element-plus/element-plus/packages/components/input/src/input.vue"]]);const Nt=dt(Pt);export{Nt as E,ft as i};
