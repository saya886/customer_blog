<template>
<div >
    <div class="main">
    <div class="title">&nbsp;&nbsp;  CuratedChina</div>
    <div class="divider"></div>
    <div class="conetnt">{{ $t('h_8')}}</div>
    </div>


    <div class="main_1">
        <div class="main_1_background">
        <div class="main_1_content">{{ $t('h_9')}}</div>
        <div class="main_1_content">{{ $t('h_10')}}</div>
        <div class="main_1_content">{{ $t('h_11')}}</div>
        <div class="main_1_content">{{ $t('h_12')}}</div>
        <div class="main_1_content"><br>{{ $t('h_13')}}</div>
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
    // background: red;
    height: 400px;
    width: 1200px;
    margin: 0 auto;
}
.title{
    padding-top: 100px;
    text-align: center;
    color: rgb(87, 87, 87);
    font-size: 30px;
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
    font-size: 16px;
    line-height: 35px;
    text-align:center;
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
    font-size: 25px;
    line-height: 45px;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
}
</style>>
