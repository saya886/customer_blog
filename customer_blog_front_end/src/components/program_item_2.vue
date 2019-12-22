<template>
  <div class="main">
      <div class="item_gird">
          <div class="item_1">
              <img class="img_1" src="../assets/img_32.png" alt="">
              Theoretica</div>
          <div class="item_2"></div>
          <div class="item_1">
              <img class="img_2" src="../assets/img_33.png" alt="">Practical</div>

            <div class="item_1_"></div>
          <div class="item_2_">
              <div class="content">
                  Try hovering over the four 
different building blocks we offered to set up your private inspiring study tour.
              </div>
          </div>
          <div class="item_1_"></div>

          <div class="item_1">
              <img class="img_3" src="../assets/img_34.png" alt="">Entrepreneurial</div>
          <div class="item_2"></div>
          <div class="item_1">
              <img class="img_2" src="../assets/img_35.png" alt="">Cultural</div>

      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    height: 1100px;
    background: rgb(221, 221, 221);
    padding-top: 82px;
}
.item_gird{
    width: 80%;
    margin: 0 auto;
    height: 940px;
    // background: gray;
}

.item_1{
    position: relative;
    width: 30%;
    float: left;
    background: rgb(49, 47, 47);
    height: 320px;
    color: white;
    font-size: 36px;
    line-height: 320px;
    text-align: center;
}
.item_2{
    position: relative;
    float: left;
    width: 40%;
    background: rgba(255, 255, 255, 0);
    height: 320px;
}

.item_1_{
    position: relative;
    width: 30%;
    float: left;
    background: rgba(255, 255, 255, 0);
    height: 320px;
}
.item_2_{
    position: relative;
    float: left;
    width: 40%;
    background: rgb(49, 47, 47);
    height: 320px;
    display: flex;
    flex-direction: row;
    align-items:center;
    justify-content:center;
    .content{
        padding: 20px;
        color: white;
        font-size: 20px;
        text-align: center;
        line-height: 50px;
        letter-spacing: 1px;
        overflow-y: hidden;
    }
}
.img_1{
    position: absolute;
    left: -60px;
    top:0px;
}
.img_2{
    position: absolute;
    right: 0px;
    top:0px;
}
.img_3{
    position: absolute;
    left: 0px;
    top:0px;
}
</style>