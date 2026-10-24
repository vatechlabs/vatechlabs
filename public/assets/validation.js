(function(root){
'use strict';
const services=['IBM i / AS400 Services','IBM i Application Development','IBM Z Mainframe Services','Web Development','App Development','Agentic AI','Let’s explore together'];
function validate(input){
 const values={},errors={};
 for(const key of ['name','email','company','service','message']) values[key]=String(input[key]??'').trim();
 const inlineControl=/[\u0000-\u001f\u007f]/;
 const bodyControl=/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
 if(values.name.length<2||values.name.length>80||!/[\p{L}]/u.test(values.name)||inlineControl.test(values.name))errors.name='Enter a name of 2–80 characters using letters. International names, spaces, apostrophes and hyphens are welcome.';
 else if(!/^[\p{L}\p{M}\s.'’\-]+$/u.test(values.name))errors.name='Use letters, spaces, apostrophes, periods or hyphens for your name.';
 const email=values.email,parts=email.split('@');
 if(email.length>254||parts.length!==2||parts[0].length>64||!parts[0]||parts[0].startsWith('.')||parts[0].endsWith('.')||parts[0].includes('..')||! /^[A-Za-z0-9.!#$%&'*+\/=?^_`{|}~-]+$/.test(parts[0])||!parts[1]||! /^(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63}$/.test(parts[1]))errors.email='Enter a valid email address, such as name@company.com.';
 if(values.company&&(values.company.length<2||values.company.length>100||inlineControl.test(values.company)||!/[\p{L}\p{N}]/u.test(values.company)))errors.company='Enter 2–100 characters for the company, or leave it blank.';
 if(!services.includes(values.service))errors.service='Select one of the listed services.';
 if(values.message.length<20||values.message.length>2000||bodyControl.test(values.message)||!/[\p{L}\p{N}]/u.test(values.message))errors.message='Describe your project in 20–2,000 characters.';
 return {values,errors};
}
const api={validate};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.VedAanValidation=api;
})(typeof globalThis!=='undefined'?globalThis:this);
