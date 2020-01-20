<template>
  <div class="main">
    <div class="title">{{ $t('a_18')}}</div>
    <div class="item_list">

      <div class="item">
        <div class="item_">
          <div class="img_icon img_icon_1"></div>
        </div>
      </div>

      <div class="item">
        <div class="item_">
          <div class="img_icon img_icon_2"></div>
        </div>
      </div>

      <div class="item">
        <div class="item_">
          <div class="img_icon img_icon_3"></div>
        </div>
      </div>

      <div class="item">
        <div class="item_">
          <div class="img_icon img_icon_4"></div>
        </div>
      </div>

      <div class="item">
        <div class="item_">
          <div class="img_icon img_icon_5"></div>
        </div>
      </div>

      <div class="item">
        <div class="item_">
          <div class="img_icon img_icon_6"></div>
        </div>
      </div>

      <div class="item">
        <div class="item_">
          <div class="img_icon img_icon_7"></div>
        </div>
      </div>

      <div class="item">
        <div class="item_">
          <div class="img_icon img_icon_8"></div>
        </div>
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
    height: 900px;
    background: rgb(240, 240, 240);
    display:none;
}
.title{
  font-size: 48px;
  color: rgb(83, 83, 83);
  font-family: gillsans_light;
  padding-top: 100px;
  padding-bottom: 70px;
  text-align: center;
}
.item_list{
  position: relative;
  width: 80%;
  // background: gray;
  height: 550px;
  margin: 0 auto; 
}
.item{
  width: 25%;
  float: left;
  // height: 250px;
  margin-top:35px; 
  .item_{
    height: 250px;
    width: 250px;
    background: rgb(255, 255, 255);
    margin: 0 auto;
    border:2px solid gray;
    
    z-index: 10;
    .img_icon{
      height: 100%;
      width: 100%;
    }
    .img_icon_1{
      background:url("../assets/img_23.png") no-repeat center center;
    }
    .img_icon_2{
      background:url("../assets/img_24.png") no-repeat center center;
    }
    .img_icon_3{
      background:url("../assets/img_25.png") no-repeat center center;
    }
    .img_icon_4{
      background:url("../assets/img_26.png") no-repeat center center;
    }
    .img_icon_5{
      background:url("../assets/img_27.png") no-repeat center center;
    }
    .img_icon_6{
      background:url("../assets/img_28.png") no-repeat center center;
    }
    .img_icon_7{
      background:url("../assets/img_29.png") no-repeat center center;
    }
    .img_icon_8{
      background:url("../assets/img_30.png") no-repeat center center;
    }
  }
}
</style>