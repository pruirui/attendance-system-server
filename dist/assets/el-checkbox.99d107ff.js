import{d as fe,c as he,i as ke,U as F}from"./event.caa1cd05.js";import{aG as U,aH as J,I as pe,C as ge,L as xe,F as ye,K as Ce,aI as Se,ar as Q,aD as A,as as K,R as N,ag as I,X as p,aJ as G,aK as Le,aL as D,Y as X,aM as Y,a0 as Z,W as _,r as T,U as E,V as Be,aN as M,aq as H,aO as j,d as L,aP as ee,$ as O,a as y,aa as ae,w as ne,e as q,n as w,aQ as $,l as i,c as C,a1 as V,q as x,au as P,ab as Ee,x as le,t as te,aw as z,aR as oe,a8 as R,av as Ie,aS as we,aT as $e,at as Ve,Z as Fe,aE as Ne,aF as se}from"./index.9c52b99a.js";import{i as Ge}from"./index.921ddcd1.js";import{f as Te}from"./flatten.f7ca8560.js";function ie(e){return e}function ze(e,a,l){switch(l.length){case 0:return e.call(a);case 1:return e.call(a,l[0]);case 2:return e.call(a,l[0],l[1]);case 3:return e.call(a,l[0],l[1],l[2])}return e.apply(a,l)}var De=800,Oe=16,Pe=Date.now;function Re(e){var a=0,l=0;return function(){var n=Pe(),s=Oe-(n-l);if(l=n,s>0){if(++a>=De)return arguments[0]}else a=0;return e.apply(void 0,arguments)}}function Ue(e){return function(){return e}}var Ae=U?function(e,a){return U(e,"toString",{configurable:!0,enumerable:!1,value:Ue(a),writable:!0})}:ie;const Ke=Ae;var Me=Re(Ke);const ue=Me;var W=Math.max;function re(e,a,l){return a=W(a===void 0?e.length-1:a,0),function(){for(var n=arguments,s=-1,d=W(n.length-a,0),c=Array(d);++s<d;)c[s]=n[a+s];s=-1;for(var t=Array(a+1);++s<a;)t[s]=n[s];return t[a]=l(c),ze(e,this,t)}}function ya(e,a){return ue(re(e,a,ie),e+"")}function He(e){return ue(re(e,void 0,Te),e+"")}function qe(e,a){return e!=null&&a in Object(e)}function We(e,a,l){a=J(a,e);for(var n=-1,s=a.length,d=!1;++n<s;){var c=pe(a[n]);if(!(d=e!=null&&l(e,c)))break;e=e[c]}return d||++n!=s?d:(s=e==null?0:e.length,!!s&&fe(s)&&ge(c,s)&&(xe(e)||he(e)))}function Je(e,a){return e!=null&&We(e,a,qe)}function Ca(e){return ye(e)&&ke(e)}function Qe(e,a,l){for(var n=-1,s=a.length,d={};++n<s;){var c=a[n],t=Ce(e,c);l(t,c)&&Se(d,J(c,e),t)}return d}function Xe(e,a){return Qe(e,a,function(l,n){return Je(e,n)})}var Ye=He(function(e,a){return e==null?{}:Xe(e,a)});const Ze=Ye,de={modelValue:{type:[Number,String,Boolean],default:void 0},label:{type:[String,Boolean,Number,Object]},indeterminate:Boolean,disabled:Boolean,checked:Boolean,name:{type:String,default:void 0},trueLabel:{type:[String,Number],default:void 0},falseLabel:{type:[String,Number],default:void 0},id:{type:String,default:void 0},controls:{type:String,default:void 0},border:Boolean,size:Q,tabindex:[String,Number],validateEvent:{type:Boolean,default:!0}},ce={[F]:e=>A(e)||K(e)||N(e),change:e=>A(e)||K(e)||N(e)},B=Symbol("checkboxGroupContextKey"),_e=({model:e,isChecked:a})=>{const l=I(B,void 0),n=p(()=>{var d,c;const t=(d=l==null?void 0:l.max)==null?void 0:d.value,m=(c=l==null?void 0:l.min)==null?void 0:c.value;return!G(t)&&e.value.length>=t&&!a.value||!G(m)&&e.value.length<=m&&a.value});return{isDisabled:Le(p(()=>(l==null?void 0:l.disabled.value)||n.value)),isLimitDisabled:n}},je=(e,{model:a,isLimitExceeded:l,hasOwnLabel:n,isDisabled:s,isLabeledByFormItem:d})=>{const c=I(B,void 0),{formItem:t}=D(),{emit:m}=_();function o(r){var b,v;return r===e.trueLabel||r===!0?(b=e.trueLabel)!=null?b:!0:(v=e.falseLabel)!=null?v:!1}function f(r,b){m("change",o(r),b)}function k(r){if(l.value)return;const b=r.target;m("change",o(b.checked),r)}async function S(r){l.value||!n.value&&!s.value&&d.value&&(r.composedPath().some(h=>h.tagName==="LABEL")||(a.value=o([!1,e.falseLabel].includes(a.value)),await Z(),f(a.value,r)))}const u=p(()=>(c==null?void 0:c.validateEvent)||e.validateEvent);return X(()=>e.modelValue,()=>{u.value&&(t==null||t.validate("change").catch(r=>Y()))}),{handleChange:k,onClickRoot:S}},ea=e=>{const a=T(!1),{emit:l}=_(),n=I(B,void 0),s=p(()=>G(n)===!1),d=T(!1);return{model:p({get(){var t,m;return s.value?(t=n==null?void 0:n.modelValue)==null?void 0:t.value:(m=e.modelValue)!=null?m:a.value},set(t){var m,o;s.value&&E(t)?(d.value=((m=n==null?void 0:n.max)==null?void 0:m.value)!==void 0&&t.length>(n==null?void 0:n.max.value),d.value===!1&&((o=n==null?void 0:n.changeEvent)==null||o.call(n,t))):(l(F,t),a.value=t)}}),isGroup:s,isLimitExceeded:d}},aa=(e,a,{model:l})=>{const n=I(B,void 0),s=T(!1),d=p(()=>{const o=l.value;return N(o)?o:E(o)?Be(e.label)?o.map(M).some(f=>Ge(f,e.label)):o.map(M).includes(e.label):o!=null?o===e.trueLabel:!!o}),c=H(p(()=>{var o;return(o=n==null?void 0:n.size)==null?void 0:o.value}),{prop:!0}),t=H(p(()=>{var o;return(o=n==null?void 0:n.size)==null?void 0:o.value})),m=p(()=>!!(a.default||e.label));return{checkboxButtonSize:c,isChecked:d,isFocused:s,checkboxSize:t,hasOwnLabel:m}},na=(e,{model:a})=>{function l(){E(a.value)&&!a.value.includes(e.label)?a.value.push(e.label):a.value=e.trueLabel||!0}e.checked&&l()},be=(e,a)=>{const{formItem:l}=D(),{model:n,isGroup:s,isLimitExceeded:d}=ea(e),{isFocused:c,isChecked:t,checkboxButtonSize:m,checkboxSize:o,hasOwnLabel:f}=aa(e,a,{model:n}),{isDisabled:k}=_e({model:n,isChecked:t}),{inputId:S,isLabeledByFormItem:u}=j(e,{formItemContext:l,disableIdGeneration:f,disableIdManagement:s}),{handleChange:r,onClickRoot:b}=je(e,{model:n,isLimitExceeded:d,hasOwnLabel:f,isDisabled:k,isLabeledByFormItem:u});return na(e,{model:n}),{inputId:S,isLabeledByFormItem:u,isChecked:t,isDisabled:k,isFocused:c,checkboxButtonSize:m,checkboxSize:o,hasOwnLabel:f,model:n,handleChange:r,onClickRoot:b}},la=["tabindex","role","aria-checked"],ta=["id","aria-hidden","name","tabindex","disabled","true-value","false-value"],oa=["id","aria-hidden","disabled","value","name","tabindex"],sa=L({name:"ElCheckbox"}),ia=L({...sa,props:de,emits:ce,setup(e){const a=e,l=ee(),{inputId:n,isLabeledByFormItem:s,isChecked:d,isDisabled:c,isFocused:t,checkboxSize:m,hasOwnLabel:o,model:f,handleChange:k,onClickRoot:S}=be(a,l),u=O("checkbox"),r=p(()=>[u.b(),u.m(m.value),u.is("disabled",c.value),u.is("bordered",a.border),u.is("checked",d.value)]),b=p(()=>[u.e("input"),u.is("disabled",c.value),u.is("checked",d.value),u.is("indeterminate",a.indeterminate),u.is("focus",t.value)]);return(v,h)=>(y(),ae(oe(!i(o)&&i(s)?"span":"label"),{class:x(i(r)),"aria-controls":v.indeterminate?v.controls:null,onClick:i(S)},{default:ne(()=>[q("span",{class:x(i(b)),tabindex:v.indeterminate?0:void 0,role:v.indeterminate?"checkbox":void 0,"aria-checked":v.indeterminate?"mixed":void 0},[v.trueLabel||v.falseLabel?w((y(),C("input",{key:0,id:i(n),"onUpdate:modelValue":h[0]||(h[0]=g=>V(f)?f.value=g:null),class:x(i(u).e("original")),type:"checkbox","aria-hidden":v.indeterminate?"true":"false",name:v.name,tabindex:v.tabindex,disabled:i(c),"true-value":v.trueLabel,"false-value":v.falseLabel,onChange:h[1]||(h[1]=(...g)=>i(k)&&i(k)(...g)),onFocus:h[2]||(h[2]=g=>t.value=!0),onBlur:h[3]||(h[3]=g=>t.value=!1)},null,42,ta)),[[$,i(f)]]):w((y(),C("input",{key:1,id:i(n),"onUpdate:modelValue":h[4]||(h[4]=g=>V(f)?f.value=g:null),class:x(i(u).e("original")),type:"checkbox","aria-hidden":v.indeterminate?"true":"false",disabled:i(c),value:v.label,name:v.name,tabindex:v.tabindex,onChange:h[5]||(h[5]=(...g)=>i(k)&&i(k)(...g)),onFocus:h[6]||(h[6]=g=>t.value=!0),onBlur:h[7]||(h[7]=g=>t.value=!1)},null,42,oa)),[[$,i(f)]]),q("span",{class:x(i(u).e("inner"))},null,2)],10,la),i(o)?(y(),C("span",{key:0,class:x(i(u).e("label"))},[P(v.$slots,"default"),v.$slots.default?z("v-if",!0):(y(),C(Ee,{key:0},[le(te(v.label),1)],64))],2)):z("v-if",!0)]),_:3},8,["class","aria-controls","onClick"]))}});var ua=R(ia,[["__file","/home/runner/work/element-plus/element-plus/packages/components/checkbox/src/checkbox.vue"]]);const ra=["name","tabindex","disabled","true-value","false-value"],da=["name","tabindex","disabled","value"],ca=L({name:"ElCheckboxButton"}),ba=L({...ca,props:de,emits:ce,setup(e){const a=e,l=ee(),{isFocused:n,isChecked:s,isDisabled:d,checkboxButtonSize:c,model:t,handleChange:m}=be(a,l),o=I(B,void 0),f=O("checkbox"),k=p(()=>{var u,r,b,v;const h=(r=(u=o==null?void 0:o.fill)==null?void 0:u.value)!=null?r:"";return{backgroundColor:h,borderColor:h,color:(v=(b=o==null?void 0:o.textColor)==null?void 0:b.value)!=null?v:"",boxShadow:h?`-1px 0 0 0 ${h}`:void 0}}),S=p(()=>[f.b("button"),f.bm("button",c.value),f.is("disabled",d.value),f.is("checked",s.value),f.is("focus",n.value)]);return(u,r)=>(y(),C("label",{class:x(i(S))},[u.trueLabel||u.falseLabel?w((y(),C("input",{key:0,"onUpdate:modelValue":r[0]||(r[0]=b=>V(t)?t.value=b:null),class:x(i(f).be("button","original")),type:"checkbox",name:u.name,tabindex:u.tabindex,disabled:i(d),"true-value":u.trueLabel,"false-value":u.falseLabel,onChange:r[1]||(r[1]=(...b)=>i(m)&&i(m)(...b)),onFocus:r[2]||(r[2]=b=>n.value=!0),onBlur:r[3]||(r[3]=b=>n.value=!1)},null,42,ra)),[[$,i(t)]]):w((y(),C("input",{key:1,"onUpdate:modelValue":r[4]||(r[4]=b=>V(t)?t.value=b:null),class:x(i(f).be("button","original")),type:"checkbox",name:u.name,tabindex:u.tabindex,disabled:i(d),value:u.label,onChange:r[5]||(r[5]=(...b)=>i(m)&&i(m)(...b)),onFocus:r[6]||(r[6]=b=>n.value=!0),onBlur:r[7]||(r[7]=b=>n.value=!1)},null,42,da)),[[$,i(t)]]),u.$slots.default||u.label?(y(),C("span",{key:2,class:x(i(f).be("button","inner")),style:Ie(i(s)?i(k):void 0)},[P(u.$slots,"default",{},()=>[le(te(u.label),1)])],6)):z("v-if",!0)],2))}});var ve=R(ba,[["__file","/home/runner/work/element-plus/element-plus/packages/components/checkbox/src/checkbox-button.vue"]]);const va=we({modelValue:{type:$e(Array),default:()=>[]},disabled:Boolean,min:Number,max:Number,size:Q,label:String,fill:String,textColor:String,tag:{type:String,default:"div"},validateEvent:{type:Boolean,default:!0}}),ma={[F]:e=>E(e),change:e=>E(e)},fa=L({name:"ElCheckboxGroup"}),ha=L({...fa,props:va,emits:ma,setup(e,{emit:a}){const l=e,n=O("checkbox"),{formItem:s}=D(),{inputId:d,isLabeledByFormItem:c}=j(l,{formItemContext:s}),t=async o=>{a(F,o),await Z(),a("change",o)},m=p({get(){return l.modelValue},set(o){t(o)}});return Ve(B,{...Ze(Fe(l),["size","min","max","disabled","validateEvent","fill","textColor"]),modelValue:m,changeEvent:t}),X(()=>l.modelValue,()=>{l.validateEvent&&(s==null||s.validate("change").catch(o=>Y()))}),(o,f)=>{var k;return y(),ae(oe(o.tag),{id:i(d),class:x(i(n).b("group")),role:"group","aria-label":i(c)?void 0:o.label||"checkbox-group","aria-labelledby":i(c)?(k=i(s))==null?void 0:k.labelId:void 0},{default:ne(()=>[P(o.$slots,"default")]),_:3},8,["id","class","aria-label","aria-labelledby"])}}});var me=R(ha,[["__file","/home/runner/work/element-plus/element-plus/packages/components/checkbox/src/checkbox-group.vue"]]);const Sa=Ne(ua,{CheckboxButton:ve,CheckboxGroup:me});se(ve);const La=se(me);export{Sa as E,Ca as a,ya as b,La as c,Je as h,ie as i};