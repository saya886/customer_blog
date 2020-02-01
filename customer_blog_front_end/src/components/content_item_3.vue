<template>



<div class="main">
    <div class="main_item main_item_1">
        <div class="main_content">
        <div class="main_text">{{ $t('h_32')}}</div>
        <div class="main_text">{{ $t('h_33')}}</div>
        <div class="main_text">{{ $t('h_34')}}</div>
        <div class="main_text">{{ $t('h_35')}}</div>
        </div>
    </div>
    <div class="main_item main_item_2">
        <div class="main_content">
        <div class="main_text">{{ $t('h_36')}}</div>
        <div class="main_text">{{ $t('h_37')}}</div>
        <div class="main_text">{{ $t('h_38')}}</div>
        <div class="main_text">{{ $t('h_39')}}</div>
        </div>
    </div>
    <div class="main_item main_item_3">
        <div class="main_content">
        <div class="main_text">{{ $t('h_40')}}</div>
        <div class="main_text">{{ $t('h_41')}}</div>
        <div class="main_text">{{ $t('h_42')}}</div>
        <div class="main_text">{{ $t('h_43')}}</div>
        </div>
    </div>
    
 
    <div class="main_item main_item_4">
        <div class="main_content">
        <div class="main_text">{{ $t('h_44')}}</div>
        <div class="main_text">{{ $t('h_45')}}</div>
        <div class="main_text">{{ $t('h_46')}}</div>
        </div>
    </div>
</div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main_item{
    // background: rgba(9, 255, 0, 0.445);
    height: 512px;
    padding-top: 130px; 
    .main_content{
        
        background: rgba(0, 0, 0, 0.507);
        width: 760px;
        margin: 0 auto;
        padding: 50px; 
    }
    .main_text{
        color: white;
        font-size: 16px;
        line-height: 45px;
        text-align: center;
        letter-spacing:1px;
    }
    
}
.main_item_1{
    background:url("../assets/img_2.png") no-repeat center center;
    background-size: cover;
}
.main_item_2{
    background:url("../assets/img_3.png") no-repeat center center;
    background-size: cover;
}
.main_item_3{
    background:url("../assets/img_4.png") no-repeat center center;
    background-size: cover;
}
.main_item_4{
    background:url("../assets/img_5.png") no-repeat center center;
    background-size: cover;
}
</style>>
