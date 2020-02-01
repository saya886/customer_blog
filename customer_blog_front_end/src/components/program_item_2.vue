<template>
  <div class="main">
      <div class="item_gird">
          <div class="item_1">
              <img class="img_1" src="../assets/img_32.png" alt="">
              <div class="img_abs"><img class="inline_img" src="../assets/img_39.png"><span class="index_count">I :</span></div>
              {{ $t('p_3')}}</div>
          <div class="item_2"></div>
          <div class="item_1">
              <img class="img_2" src="../assets/img_33.png" alt="">
              <div class="img_abs_1"><img class="inline_img" src="../assets/img_39.png"><span class="index_count">Ⅱ :</span></div>
              {{ $t('p_4')}}</div>

            <div class="item_1_"></div>
          <div class="item_2_">
              <div class="content">
                  {{ $t('p_5')}}
              </div>
          </div>
          <div class="item_1_"></div>

          <div class="item_1">
              <img class="img_3" src="../assets/img_34.png" alt="">
              <div class="img_abs_2"><img class="inline_img" src="../assets/img_39.png"><span class="index_count">Ⅲ :</span></div>
              {{ $t('p_6')}}</div>
          <div class="item_2"></div>
          <div class="item_1">
              <img class="img_2" src="../assets/img_35.png" alt="">
              <div class="img_abs_3"><img class="inline_img" src="../assets/img_39.png"><span class="index_count">Ⅳ:</span></div>
              {{ $t('p_7')}}</div>

      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    height: 750px;
    background: rgb(221, 221, 221);
    padding-top: 82px;
}
.item_gird{
    width: 80%;
    margin: 0 auto;
    height: 540px;
    // background: gray;
}

.item_1{
    position: relative;
    width: 30%;
    float: left;
    background: rgb(49, 47, 47);
    height: 220px;
    color: white;
    font-size: 25px;
    line-height: 220px;
    text-align: center;
}
.item_2{
    position: relative;
    float: left;
    width: 40%;
    background: rgba(255, 255, 255, 0);
    height: 220px;
}

.item_1_{
    position: relative;
    width: 30%;
    float: left;
    background: rgba(255, 255, 255, 0);
    height: 220px;
}
.item_2_{
    position: relative;
    float: left;
    width: 40%;
    background: rgb(49, 47, 47);
    height: 220px;
    display: flex;
    flex-direction: row;
    align-items:center;
    justify-content:center;
    .content{
        padding: 20px;
        color: white;
        font-size: 16px;
        text-align: center;
        line-height: 35px;
        letter-spacing: 1px;
        overflow-y: hidden;
    }
}
.img_1{
    position: absolute;
    left: -60px;
    top:0px;
    // height:220px;
}
.img_2{
    position: absolute;
    right: 0px;
    bottom:0px;
    height:220px;
}
.img_3{
    position: absolute;
    left: 0px;
    top:0px;
    height:220px;
}
.inline_img{
    display:inline;
}
.index_count{
    font-size:15px;
    margin-left:10px;
}
.img_abs{
    position:absolute;
    top:-39px;
    left:45%;
}
.img_abs_1{
    position:absolute;
    top:-39px;
    left:45%;
}
.img_abs_2{
    position:absolute;
    top:-39px;
    left:45%;
}
.img_abs_3{
    position:absolute;
    top:-39px;
    left:45%;
}
</style>