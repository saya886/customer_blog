<template>
  <div class="main">
    <div class="t_1">{{ $t('a_14')}}</div>
    <div class="t_2">{{ $t('a_15')}}</div>
    <div class="t_1">{{ $t('a_16')}}</div>
    <div class="t_2">{{ $t('a_17')}}</div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    height: 550px;
    background: gray;
    background:url("../assets/img_22.png") no-repeat center center;
    background-size: cover;
    padding-bottom: 100px;
}
.t_1{
  color: aliceblue;
  font-size: 25px;
  font-family: gillsans_light;
  text-align: center;
  padding-top: 130px;
  letter-spacing:1px;
}
.t_2{
  color: aliceblue;
  font-size: 16px;
  font-family: gillsans_light;
  text-align: center;
  padding-top: 30px;
  width: 70%;
  margin: 0 auto;
  line-height: 40px;
  letter-spacing:1px;
}
</style>