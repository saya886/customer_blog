<template>
<div :style="{height:height_+'px'}" class="main">
    
    <div class="content_1">
        <div :style="{'margin-top':top_pad+'px'}" class="title_1 title">{{ $t('h_1')}}</div>
        <div class="title">{{ $t('h_2')}}</div>
        <div class="divider"></div>
        <div class="icon_group">
            <div class="icon_ietm">
                <div class="icon_image icon_image_edu"></div>
                <div class="icon_content">
                    {{ $t('h_3')}}
                </div>
            </div>
            <div class="icon_ietm">
                <div class="icon_image icon_image_ins"></div>
                <div class="icon_content">
                    {{ $t('h_4')}}
                </div>
            </div>
            <div class="icon_ietm">
                <div class="icon_image icon_image_dyn"></div>
                <div class="icon_content">
                    {{ $t('h_5')}}
                </div>
            </div>
        </div>
        <div @click="change_route('programs#1_id')" class="center_button">{{ $t('h_6')}}</div>
    </div>
</div>
</template>

<script>
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
                this.top_pad = height_doc*0.185
            }
        }
    },
    methods:{
        change_route(path){
            this.$router.push("/" + path)
        }
    }
}
</script>

<style lang="less" scoped>
.main{
    height: 700px;
    background: gray;
    background:url("../assets/img_40.jpg") no-repeat center center;
    background-size: cover;
    // overflow-y:hidden;
    padding-top:80px;
}


.title{
    // background: red;
    
    margin: 0 auto;
    margin-top: 10px;
    width: 1000px;  
    height: 60px;
    font-size: 30px;
    color: white;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
}
.title_1{
    margin-top:130px; 
}
.divider{
    background: red;
    
    margin: 0 auto;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-left:-8px;
    width: 100%;  
    height: 15px;
    background:url("../assets/divider_1_white.png") no-repeat center center;
}
.icon_group{
    // background: red;
    
    margin: 0 auto;
    margin-top: 20px;
    width: 550px;  
    height: 110px;
    // padding: 5px;
    .icon_ietm{
        display: inline-block;
        // background: green;
        width: 32%;
        height: 100%;
        padding: 2px;
        .icon_image{
            // background: red;
            height: 100px;
            transform: scale(0.7,0.7); /* 标准语法 */
            
        }
        .icon_image_edu{
            background:url("../assets/edu.png") no-repeat center;
        }
        .icon_image_ins{
            background:url("../assets/ins.png") no-repeat center;
        }
        .icon_image_dyn{
            background:url("../assets/dyn.png") no-repeat center;
        }

        .icon_image_edu:hover{
            background:url("../assets/edu_1.png") no-repeat center;
        }
        .icon_image_ins:hover{
            background:url("../assets/ins_1.png") no-repeat center;
        }
        .icon_image_dyn:hover{
            background:url("../assets/dyn_1.png") no-repeat center;
        }

        .icon_content{
            text-align: center;
            color: white;
            font-size: 16px;
            line-height: 24px;
        }

    }
}
.center_button{
    height: 35px;
    width: 130px;
    margin: 0 auto;
    margin-top: 70px; 
    
    text-align: center;
    border:3px solid white;
    line-height: 35px;
    font-size: 16px;
    color: white;
    cursor:pointer;
    
}
.center_button:hover{
    background: white;
    color: black;
}
</style>>
