
// 窗口大小
var width = window.innerWidth;
var height = window.innerHeight;
console.log("视口宽度: " + width + ", 视口高度: " + height);


// 鼠标位置
// 复制下面的脚本到浏览器的console中, "enter", 即可使用该脚本获取鼠标位置
document.addEventListener('mouseup',function(e){
    console.log(e.pageX,e.pageY);
})