<template>
<div class="main">
    <div class="main_content">
    <div class="title_1">Hello.</div>
    <div class="title_2">Let’s work together to create your fruitful learning experiences in China.</div>
    <div class="text_item text_1">
        <div class="item_group">
            <div class="icon_item icon_item_1"></div>
            <div class="value_item">Email  :  hello@curatedchina.com</div>
        </div>
    </div>
    <div class="text_item text_2">
        <div class="item_group">
            <div class="icon_item icon_item_2"></div>
            <div class="value_item">Phone  :  + 86 18001611312</div>
        </div>
    </div>
    <div class="text_item text_3">
        <div class="item_group">
            <div class="icon_item icon_item_3"></div>
            <div class="value_item">Address : Rm 3506, Building #3, No. 277 Zheqiao Rd, Shanghai, China</div>
        </div>
    </div>
    <div @click="change_route('contact#enquire')" class="button_cust">ENQUIRE</div>
    </div>

    <div class="abs_img_1"></div>
    <div class="abs_img_2"></div>
</div>
</template>

<script>
export default {
    methods:{
        change_route(path){
            this.$router.push("/" + path)
        }
    }
}
</script>

<style lang="less" scoped>
.main{
    background: rgb(66, 66, 66);
    height: 560px;
    position: relative;
}
.main_content{
     
    width:900px;
    margin: 0 auto;
    padding-top: 100px;
}
.title_1{
    color: white;
    font-size: 40px;
}
.title_2{
    margin-top:10px;
    color: white;
    font-size: 20px;
    margin-bottom:20px;
}
.text_item{
    height: 50px;
    width: 600px;
    border-bottom-style: solid;
    border-width: 2px;
    border-color:rgb(116, 116, 116);
    .item_group{
        height: 100%;
        .icon_item{
            background: red;
            height: 100%;
            width: 27px;
            // display: inline-block;
            float: left;
            margin-right: 20px; 
            
        }
        .icon_item_1{
            background:url("../assets/img_9.png") no-repeat center center;
        }
        .icon_item_2{
            background:url("../assets/img_10.png") no-repeat center center;
        }
        .icon_item_3{
            background:url("../assets/img_11.png") no-repeat center center;
        }
        .value_item{
            // background: red;
            float: left;
            color: white;
            height: 100%;
            width: 500px;
            font-size: 14px;
            line-height: 50px;
        }
    }
    
}
.button_cust{
    height: 35px;
    width: 160px;
    margin-left: 50px;
    margin-top: 70px; 
    
    text-align: center;
    border:2px solid white;
    line-height: 35px;
    font-size: 18px;
    color: white;
    cursor:pointer;
}
.button_cust:hover{
    background: white;
    color: black;
    cursor: pointer;
}
.abs_img_1{
    height: 466px;
    width: 72px;
    position: absolute;
    bottom: 0px;
    left: 80px;
    background:url("../assets/img_7.png") no-repeat center center;
}
.abs_img_2{
    // z-index: 10000000;
    height: 360px;
    width: 360px;
    position: absolute;
    bottom: -100px;
    right: 150px;
    background:url("../assets/img_8.png") no-repeat center center;
}
</style>>
