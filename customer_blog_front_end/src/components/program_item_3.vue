<template>
  <div class="main">
      <div class="content">
          <div class="text_1">Have more<br>
specific demand?</div>
          <div @click="change_route('contact#enquire')" class="button_">Contact Us</div>
          <div class="text_2">We’ll do our best<br>
to accommodate<br>
your needs!</div>
      </div>
  </div>
</template>

<script>
export default {
    methods:{
        change_route(path){
            this.$router.push(path)
        }
    }
}
</script>

<style lang="less" scoped>
.main{
    height: 800px;
    background: rgb(52, 52, 54);
    padding-top: 70px;
}
.content{
    height: 700px;
    width: 700px;
    border-radius: 50%;
    background: rgb(224, 224, 224);
    margin:0 auto;
}
.text_1{
    padding-top: 190px;
    color: rgb(39, 39, 39);
    font-size: 40px;
    line-height: 40px;
    text-align: center;
    margin-bottom: 40px;
    letter-spacing: 1px;
}
.text_2{
    margin-top: 30px;
    color: rgb(39, 39, 39);
    font-size: 40px;
    line-height: 40px;
    text-align: center;
    letter-spacing: 1px;
}
.button_{
    width: 250px;
    height: 38px;
    color: rgb(230, 230, 230);
    font-size: 25px;
    line-height: 45px;
    text-align: center;
    background: rgb(139, 7, 7);
    border-radius: 25px;
    font-family: gillsans_light;
    margin: 0 auto;
    cursor: pointer;
}
</style>