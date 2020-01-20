<template>
  <div :style="{height:height_+'px'}" class="main">
      
      <div :style="{'margin-top':top_pad+'px'}" class="title_1">{{ $t('b_1')}}<br>
{{ $t('b_2')}}</div>
  </div>
</template>

<script>
import header_menu_dark from './header_menu_dark.vue'
export default {
    data(){
        return{
            "height_":"",
            "top_pad":""
        }
    },
    mounted(){
        var userAgentInfo = navigator.userAgent;
        var Agents = new Array("Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod");  
        var flag = true;  
        for (var v = 0; v < Agents.length; v++) {  
            if (userAgentInfo.indexOf(Agents[v]) > 0) { flag = false; break; }  
        }
        if(flag){
            let height_doc = document.documentElement.clientHeight
            console.log(height_doc);
            if(height_doc > 700){
                this.height_ = height_doc
                this.top_pad = height_doc*0.257
            }
        }
    },
    components: {
        header_menu_dark
    }
}
</script>

<style lang="less" scoped>

.main{
    height: 700px;
    background: gray;
    background:url("../assets/img_36.png") no-repeat center center;
    background-size: cover;
    z-index: 100;
    padding-top:80px;
}
.title_1{
    height:50px;
    font-size: 40px;
    color: #676262;
    margin: 0 auto;
    // width: 340px;
    margin-top:180px;
    text-align: center;
    // text-shadow: 5px 5px 8px #000000;
    // background: rgba(255, 255, 255, 0.685);
    // font-weight: 100;
    line-height: 65px;
    // font-family: gillsans_light;
    letter-spacing: 1px;
}
</style>