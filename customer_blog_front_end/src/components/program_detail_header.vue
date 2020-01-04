<template>
  <div class="main">

      <div class="title">Unlock China Business Hub</div>
      <div class="title_2">Customized Schedule & Bespoke Services </div>
  </div>
</template>

<script>
import header_menu from './header_menu.vue'
export default {
    components: {
        header_menu
    }
}
</script>

<style lang="less" scoped>

.main{
    height: 700px;
    background: gray;
    background:url("../assets/img_42.jpg") no-repeat center center;
    background-size: cover;
    padding-top:80px;
}
.title{
    height:50px;
    font-size: 40px;
    color: white;
    margin: 0 auto;
    margin-top:200px;
    text-align: center;
    text-shadow: 2px 2px 8px #000000;
}
.title_2{
    height:100px;
    font-size: 23px;
    color: white;
    margin: 0 auto;
    margin-top:30px;
    text-align: center;
    text-shadow: 2px 2px 8px #000000;
}
</style>