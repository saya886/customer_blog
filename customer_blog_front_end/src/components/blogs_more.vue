<template>
  <div>
      
      <div class="sec_1">
          <div class="main">
      <div class="title">
          {{ this.$route.params.categary.toString()}}
      </div>
      <div class="left_text">INSPIRED FROM</div>
      <div class="item_list">
          <div v-for="blog in blog_list" class="item">

              <div class="item_">
                  <img  @click="go_to_detail(blog.id)" class="icon" v-bind:src="blog.blog_img" alt="">
              <div @click="go_to_detail(blog.id)" class="name">{{blog.title}}</div>
                <div class="author">{{blog.author}}</div>
              </div>
              
          </div>

      </div>
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
            url: "http://127.0.0.1:8000/blog?categary="+this.$route.params.categary.toString(),
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
        }
    }
}
</script>

<style lang="less" scoped>
.main{
    // height: 900px;
    background: rgb(248, 248, 248);
    border:1px solid rgb(26, 26, 26);
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
    margin-bottom: 100px;
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