<template>
  <div class="main">

      <div class="title_1">Our First and Foremost Goal </div>
      <div class="title_2">To create the most practical and inspiring
learning journey in China that you
treasure.</div>
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
    height: 600px;
    background: gray;
    background:url("../assets/img_31.png") no-repeat center center;
    background-size: cover;
    z-index: 100;
    padding-top:80px;
}
.title_1{
    height:70px;
    font-size: 40px;
    color: white;
    margin-top:150px;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
    font-weight: 100;
    line-height: 85px;
    font-family: gillsans_light;
}
.title_2{
    font-size: 50px;
    color: white;
    width: 70%;
    margin: 0 auto;
    margin-top:40px;
    // width: 300px;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
    letter-spacing: 2px;

}
</style>