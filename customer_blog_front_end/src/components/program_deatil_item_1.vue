<template>
  <div class="main">

    <div class="main_header">

      <div class="main_header_title">{{data.title_1}}{{data.title_2}}</div>
      <div class="main_header_title_2">{{data.desc}}</div>
  </div>

  <div class="content_container">
    <div class="title">{{data.title_1}}{{data.title_2}}</div>
    <div class="dvider"></div>
    <div v-html="data.content" class="content"></div>
  </div>

  <div class="dropdown_container">
    <div class="drop_down_item">
      <div class="drop_down_item_">
        <div class="drop_down_control">+</div>
        <div class="drop_down_title">Learning objectives</div>
        <div v-html="data.learning_objectives" class="drop_down_content"></div>
      </div>
    </div>

    <div class="drop_down_item">
      <div class="drop_down_item_">
        <div class="drop_down_control">+</div>
        <div class="drop_down_title">Itinerary</div>
        <div v-html="data.details" class="drop_down_content"></div>
      </div>
    </div>

    <div class="drop_down_item">
      <div class="drop_down_item_">
        <div class="drop_down_control">+</div>
        <div class="drop_down_title">Details</div>
        <div v-html="data.content" class="drop_down_content"></div>
      </div>
    </div>

  </div>
  </div>
</template>

<script>
export default {
data(){
  return{
      "data":{
        "title_1":"",
        "title_2":"",
        "desc":"",
        "content":"",
        "learning_objectives":"",
        "ltinerary":"",
        "details":"",
      }
  }
},
mounted(){
    this.$axios({
        method: "get",
        url: "/program?program_id=" + this.$route.params.program_id,
    }).then(response => {
        console.log(response, "success");   // 成功的返回
        this.data = response.data.data
    })
    .catch(error => {
        console.log(error, "error")
    }); // 失败的返回
},
methods:{
  
}
}
</script>

<style lang="less" scoped>
.main_header{
    height: 700px;
    background: gray;
    background:url("../assets/img_42.jpg") no-repeat center center;
    background-size: cover;
    padding-top:80px;
}
.main_header_title{
    height:50px;
    font-size: 40px;
    color: white;
    margin: 0 auto;
    margin-top:200px;
    text-align: center;
    text-shadow: 2px 2px 8px #000000;
}
.main_header_title_2{
    height:100px;
    font-size: 23px;
    color: white;
    margin: 0 auto;
    margin-top:30px;
    text-align: center;
    text-shadow: 2px 2px 8px #000000;
}

.main{
    // height: 500px;
    // background: gray;
}
.content_container{
  padding-top: 100px;
  padding-bottom: 60px;
  width:70%;
  margin: 0 auto;
}
.title{
  text-align:center;
  font-size: 30px;
  color: #3e3e3e;
  
  text-align: center;
  font-family: gillsans_light;
  letter-spacing: 1px;
}
.content{
  text-align:center;
  color: #3e3e3e;
  font-family: gillsans_light;
}
.dvider{
    background: red;
    
    margin: 0 auto;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-left:-8px;
    width: 100%;  
    height: 15px;
    background:url("../assets/divider_red.jpg") no-repeat center center;
}
.dropdown_container{
  border-top:2px solid #989898;
  padding-bottom: 100px;
}
.drop_down_item{

  border-bottom:2px solid #989898;
  width:100%;
  .drop_down_item_{
    width:80%;
    margin:0 auto;
    position:relative;
    .drop_down_title{
      font-size:25px;
      line-height:60px;
      font-family: gillsans_light;
      height:50px;
      // border-bottom:2px solid gray;
    }
    .drop_down_control{
      position:absolute;
      right:0px;
      font-size:30px;
      line-height:60px;
      font-family: gillsans_light;
      cursor: pointer;
      color:#c50000;
    }
    .drop_down_content{
      margin-top:30px;
      margin-bottom:30px;
      display:none;
      // transition:display 2s;
    }
  }
}
.drop_down_item:hover{
  .drop_down_content{
    display:block;
  }
}
</style>