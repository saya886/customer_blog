<template>
  <div :style="{height:height_+'px'}" class="main">

      <div :style="{'margin-top':top_pad+'px'}" class="title_1">{{ $t('p_1')}}</div>
      <div class="title_2">{{ $t('p_2')}}</div>
  </div>
</template>

<script>
import header_menu from './header_menu.vue'
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
                this.top_pad = height_doc*0.285
            }
        }
    },
    components: {
        header_menu
    }
}
</script>

<style lang="less" scoped>

.main{
    height: 700px;
    background: gray;
    background:url("../assets/img_31.png") no-repeat center center;
    background-size: cover;
    z-index: 100;
    padding-top:80px;
}
.title_1{
    height:50px;
    font-size: 30px;
    color: white;
    margin-top:200px;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
    font-weight: 100;
    line-height: 85px;
    font-family: gillsans_light;
}
.title_2{
    font-size: 20px;
    color: white;
    width: 70%;
    margin: 0 auto;
    margin-top:40px;
    // width: 300px;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
    letter-spacing: 2px;

}
</style>