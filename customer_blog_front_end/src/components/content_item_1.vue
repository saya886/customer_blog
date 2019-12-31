<template>
<div >
    <div class="main">
    <div class="title">&nbsp;&nbsp;  CuratedChina</div>
    <div class="divider"></div>
    <dir class="conetnt">Design, organize and facilitate tailor-made in-depth study tours around China for all academics and institutions worldwide. We specialize in offering practical interactions with various enterprises and entrepreneurs operated in China to equip you with the latest insights from the Chinese market.</dir>
    </div>


    <dir class="main_1">
        <div class="main_1_background">
        <div class="main_1_content">Confucius, an ancient Chinese sage, said</div>
        <div class="main_1_content">“ Is it not a pleasure to study and practice what you have learned ？ </div>
        <div class="main_1_content">Is it not a delight after all to have friends come from afar ？”</div>
        <div class="main_1_content">“ 学而时习之，不亦说乎？有朋自远方来，不亦乐乎？”</div>
        <div class="main_1_content"><br>-  孔子</div>
        </div> 
    </dir>
</div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    // background: red;
    height: 650px;
    width: 1200px;
    margin: 0 auto;
}
.title{
    padding-top: 150px;
    text-align: center;
    color: rgb(87, 87, 87);
    font-size: 40px;
}
.divider{
    background: green;
    
    margin: 0 auto;
    margin-top: 30px;
    margin-bottom: 60px;
    width: 1211px;  
    height: 15px;
    background:url("../assets/divider_1_black.png") no-repeat center center;
}
.conetnt{
    color: rgb(83, 83, 83);
    font-size: 25px;
    line-height: 35px;
}
.main_1{
    // background: red;
    background:url("../assets/img_41.jpg") no-repeat center center;
    background-size: cover;
    height: 750px;
    
    
}
.main_1_background{
    padding-top: 260px;
    // width: 1000px;
    margin: 0 auto;
    height: 100%;
}
.main_1_content{
    color: white;
    font-size: 30px;
    line-height: 45px;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
}
</style>>
