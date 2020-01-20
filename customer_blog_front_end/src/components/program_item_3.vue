<template>
  <div class="main">
      <div class="content">
          <div class="text_1">{{ $t('p_8')}}<br>
{{ $t('p_9')}}</div>
          <div @click="change_route('contact#enquire')" class="button_">{{ $t('p_10')}}</div>
          <div class="text_2">{{ $t('p_11')}}<br>
{{ $t('p_12')}}<br>
{{ $t('p_13')}}</div>
      </div>
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
    height: 570px;
    background: rgb(52, 52, 54);
    padding-top: 70px;
}
.content{
    height: 500px;
    width: 500px;
    border-radius: 50%;
    background: rgb(224, 224, 224);
    margin:0 auto;
}
.text_1{
    padding-top: 110px;
    color: rgb(39, 39, 39);
    font-size: 20px;
    line-height: 40px;
    text-align: center;
    margin-bottom: 10px;
    letter-spacing: 1px;
    font-family:gillsans_light;
}
.text_2{
    margin-top: 10px;
    color: rgb(39, 39, 39);
    font-size: 20px;
    line-height: 40px;
    text-align: center;
    letter-spacing: 1px;
    font-family:gillsans_light;
}
.button_{
    width: 250px;
    height: 38px;
    color: rgb(230, 230, 230);
    font-size: 20px;
    line-height: 45px;
    text-align: center;
    background: rgb(139, 7, 7);
    border-radius: 25px;
    font-family: gillsans_light;
    margin: 0 auto;
    cursor: pointer;
}
</style>