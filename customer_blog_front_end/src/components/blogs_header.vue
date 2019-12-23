<template>
  <div class="main">
      <header_menu_dark/>
      <div class="title_1">Explore China with Us<br>
Stories. Inspirations. Moments</div>
  </div>
</template>

<script>
import header_menu_dark from './header_menu_dark.vue'
export default {
    components: {
        header_menu_dark
    }
}
</script>

<style lang="less" scoped>

.main{
    height: 899px;
    background: gray;
    background:url("../assets/img_36.png") no-repeat center center;
    background-size: cover;
    z-index: 100;
}
.title_1{
    height:70px;
    font-size: 50px;
    color: rgb(39, 39, 39);
    margin: 0 auto;
    // width: 340px;
    margin-top:250px;
    text-align: center;
    // text-shadow: 5px 5px 8px #000000;
    // background: rgba(255, 255, 255, 0.685);
    font-weight: 100;
    line-height: 85px;
    font-family: gillsans_light;
    letter-spacing: 1px;
}
</style>