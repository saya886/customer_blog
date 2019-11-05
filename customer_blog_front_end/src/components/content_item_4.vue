<template>
<div class="main">
    <div class="item">
        <div class="title">Testimonials</div>
        <div class="divider"></div>
        <div class="text_item">“We specialize in offering practical interactions with various
enterprises and entrepreneurs operated in China to equip you with the latest insights from the Chinese market.”</div>
        <div class="icon_group">
            <div class="icon_ietm">
                <div class="icon_image icon_image_edu"></div>
                <div class="icon_content">
                    陈俊吉<br/>行知中国执行长<br/>北大清华
                </div>
            </div>
            <div class="icon_ietm">
                <div class="icon_image icon_image_ins"></div>
                <div class="icon_content">
                    陈俊吉<br/>行知中国执行长<br/>北大清华
                </div>
            </div>
            <div class="icon_ietm">
                <div class="icon_image icon_image_dyn"></div>
                <div class="icon_content">
                    陈俊吉<br/>行知中国执行长<br/>北大清华
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    // background: rgba(255, 0, 0, 0.445);
    height: 1040px;
    padding: 150px 140px 150px 140px;
}
.item{
    // background: rgba(0, 0, 255, 0.384);
    height: 100%;
    border:3px solid rgb(136, 136, 136);
    // padding: 80px;  
}
.title{
    margin-top: 80px;
    text-align: center;
    color: rgb(82, 82, 82);
    font-size: 36px;
}
.divider{
    // background: green;
    
    margin: 0 auto;
    margin-top: 30px;
    margin-bottom: 60px;
    width: 100%;  
    height: 15px;
    background:url("../assets/divider_1_black.png") no-repeat center center;
}
.text_item{
    text-align: center;
    color: rgb(82, 82, 82);;
    font-size: 24px;
    line-height: 45px;
    width: 650px;
    margin: 0 auto;
}
.icon_group{
    // background: red;
    
    margin: 0 auto;
    margin-top: 250px;
    width: 100%;  
    height: 300px;
    // padding: 5px;
    .icon_ietm{
        display: inline-block;
        // background: green;
        width: 32.8%;
        height: 100%;
        padding: 2px;
        .icon_image{
            // background: red;
            height: 214px;
            // opacity:0.4;
            
        }
        .icon_image_edu{
            background:url("../assets/img_6.png") no-repeat center;
        }
        .icon_image_ins{
            background:url("../assets/img_6.png") no-repeat center;
        }
        .icon_image_dyn{
            background:url("../assets/img_6.png") no-repeat center;
        }
        // .icon_image:hover{
        //     opacity:1;
        // }
        .icon_content{
            margin-top: 20px; 
            text-align: center;
            color: rgb(82, 82, 82);;
            font-size: 12px;
            line-height: 24px;
        }

    }
    
}
</style>>
