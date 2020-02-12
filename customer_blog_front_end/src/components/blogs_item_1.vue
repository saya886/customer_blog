<template>
  <div>
      
      <div v-for="cate in blog_list" class="sec_1">
          <div class="main">
      <div class="title">
          {{ cate.name}}
      </div>
      <div class="left_text">{{ cate.desc}}</div>
      <div class="item_list">
          <div v-for="blog in cate.data" class="item">

              <div class="item_">
                  <img  @click="go_to_detail(blog.id)" class="icon" v-bind:src="blog.blog_img" alt="">
              <div @click="go_to_detail(blog.id)" class="name">{{blog.title}}</div>
                <div class="author">{{blog.author}}</div>
              </div>
              
          </div>

      </div>

      <div @click="go_to_more(cate.name)" class="center_button">More</div>
        </div>
      </div>


  </div>
</template>

<script>
export default {
    data(){
        return{
            "blog_list":[]
        }
    },
    mounted (){
        this.$axios({
            method: "get",
            url: "/blog?type_categary=123",
        }).then(response => {
            console.log(response, "success");   // 成功的返回
            this.blog_list = response["data"]["data"]
        })
        .catch(error => {
            console.log(error, "error")
        }); // 失败的返回
    },
    methods:{
        go_to_detail(blog_id){
            console.log(blog_id);
            this.$router.push("/blogs/"+blog_id.toString()+"#main")
        },
        go_to_more(categary_id){
            console.log(categary_id);
            this.$router.push("/categary/"+categary_id.toString()+"#main")
        }
    }
}
</script>

<style lang="less" scoped>
.main{
    height: 900px;
    background: rgb(248, 248, 248);
    border:1px solid rgb(26, 26, 26);
    // display:none;
}
.sec_1{
    position: relative;
}
.title{
    font-family: gillsans_light;
    color: rgb(49, 49, 49);
    font-size: 36px;
    text-align: center;
    letter-spacing: 1px;

    padding-top: 130px;
    padding-bottom: 90px;
}
.item_list{
    width: 80%;
    margin: 0 auto;
}
.item{
    width: 32%;
    display: inline-block;
    // background: red;
    .item_{
        width: 70%;
        margin: 0 auto;
        // background: red;
        .icon{
            width: 100%;
            // height: 200px;
            cursor: pointer;
        }
        .name{
            margin-top: 10px;
            font-family: gillsans;
            color: rgb(49, 49, 49);
            font-size: 24px;
            line-height: 30px;
            // text-align: justify;
            // letter-spacing: 1px;
            padding-bottom:10px; 
            border-bottom:1px solid rgb(26, 26, 26);
            cursor: pointer;
        }
        .author{
            margin-top: 20px;
            font-family: gillsans_light;
            color: rgb(49, 49, 49);
            font-size: 18px;
        }
    }
}
.center_button{
    font-family: gillsans_light;
    color: rgb(49, 49, 49);
    font-size: 24px;
    width: 172px;
    height: 57px;
    line-height: 60px;
    text-align: center;
    margin: 0 auto;
    border:1px solid rgb(26, 26, 26);
    margin-top: 118px;
    margin-bottom: 118px;
    letter-spacing: 1px;
}
.center_button:hover{
    background: rgb(49, 49, 49);
    color: white;
    cursor: pointer;
}
.left_text{
    font-family: gillsans_light;
    color: rgb(49, 49, 49);
    font-size: 14px;
    text-align: center;
    letter-spacing: 1px;
    transform: rotate(90deg);
    position: absolute;
    left: 5px;
    top: 350px;
}
// .title{
//     font-family: gillsans_light;
//     color: rgb(49, 49, 49);
//     font-size: 24px;
//     text-align: justify;
//     letter-spacing: 1px;
// }
</style>