<template>
  <div class="main">
      <header_menu/>
      <div class="title">We love to hear<br>
from you</div>
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
    height: 899px;
    background: gray;
    background:url("../assets/img_17.png") no-repeat center center;
    background-size: cover;
}
.title{
    height:100px;
    font-size: 50px;
    color: white;
    margin: 0 auto;
    margin-top:300px;
    width: 400px;
    text-align: center;
    text-shadow: 5px 5px 8px #000000;
}
</style>