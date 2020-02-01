<template>
  <div class="main">
      <img class="logo_center" src="../assets/logo.png" alt="">
      <div class="title">{{ $t('b_3')}}<br>
{{ $t('b_4')}}</div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    height: 800px;
    background: gray;
    background:url("../assets/img_38.png") no-repeat center center;
    background-size: cover;
    
}
.logo_center{
    width: 200px;
    margin: 0 auto;
    display: block;
    padding-top: 270px;
}
.title{
    font-size: 20px;
    color: rgb(218, 218, 218);
    margin-top: 45px;
    line-height: 40px;
    text-align: center;
    font-family: gillsans;
    letter-spacing: 1px;
    white-space: pre-line;
}
</style>