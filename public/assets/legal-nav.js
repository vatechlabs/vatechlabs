"use strict";
const menu=document.querySelector('.menu');const links=document.querySelector('.links');
if(menu&&links){const close=()=>{links.classList.remove('open');menu.setAttribute('aria-expanded','false')};menu.addEventListener('click',()=>{const opened=links.classList.toggle('open');menu.setAttribute('aria-expanded',String(opened))});document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});document.addEventListener('click',e=>{if(!e.target.closest('.nav'))close()});links.addEventListener('click',e=>{if(e.target.closest('a'))close()});window.addEventListener('resize',()=>{if(innerWidth>900)close()})}
const year=document.getElementById('year');if(year)year.textContent=new Date().getFullYear();
