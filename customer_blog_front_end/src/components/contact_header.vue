<template>
  <div :style="{height:height_+'px'}" class="main">

      <div :style="{'margin-top':top_pad+'px'}" class="title">{{ $t('c_1')}}<br>
{{ $t('c_2')}}</div>
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
            if(height_doc > 300){
                this.height_ = height_doc
                this.top_pad = height_doc*0.5
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
    background:url("../assets/img_17.png") no-repeat center center;
    background-size: cover;
    padding-top:80px;
}
.title{
    height:100px;
    font-size: 30px;
    color: white;
    // margin: 0 auto;
    float:left;
    margin-top:220px;
    margin-left:110px;
    // width: 400px;
    // text-align: center;
    text-shadow: 5px 5px 8px #000000;
}
</style>