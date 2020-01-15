<template>
  <div class="main">

    <div class="main_header">

      <div class="main_header_title">{{data.title_1}} {{data.title_2}}</div>
      <div class="main_header_title_2">{{data.desc}}</div>
  </div>

  <div class="content_container">
    <div class="title">{{data.title_1}} {{data.title_2}}</div>
    <div class="dvider"></div>
    <div v-html="data.content" class="content"></div>
  </div>

  <div class="dropdown_container">
    <div class="drop_down_item">
      <div  class="drop_down_item_">
        <div @click="learning_objectives_=!learning_objectives_" class="drop_down_control">+</div>
        <div @click="learning_objectives_=!learning_objectives_" class="drop_down_title">Learning objectives</div>
        <div v-show="learning_objectives_" v-html="data.learning_objectives" class="drop_down_content"></div>
      </div>
    </div>

    <div class="drop_down_item">
      <div  class="drop_down_item_">
        <div @click="ltinerary_=!ltinerary_" class="drop_down_control">+</div>
        <div @click="ltinerary_=!ltinerary_" class="drop_down_title">Itinerary</div>
        <div v-show="ltinerary_" v-html="data.ltinerary" class="drop_down_content"></div>
      </div>
    </div>

    <div class="drop_down_item">
      <div  class="drop_down_item_">
        <div @click="details_=!details_" class="drop_down_control">+</div>
        <div @click="details_=!details_" class="drop_down_title">Details</div>
        <div v-show="details_" v-html="data.details" class="drop_down_content"></div>
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
        
      },
      "learning_objectives_":false,
      "ltinerary_":false,
      "details_":false
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
  /deep/ span{
    font-size:16px;
    line-height:25px;
    font-family: gillsans_light;
  }
  /deep/ p{
    font-size:16px;
    line-height:25px;
    font-family: gillsans_light;
  }

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
      line-height:50px;
      font-family: gillsans_light;
      height:50px;
      // border-bottom:2px solid gray;
    }
    .drop_down_control{
      position:absolute;
      right:0px;
      font-size:30px;
      line-height:50px;
      font-family: gillsans_light;
      cursor: pointer;
      color:#c50000;
    }
    .drop_down_content{
      margin-top:30px;
      margin-bottom:30px;
      font-family: gillsans_light;
      /deep/ span{
    font-size:16px;
    line-height:25px;
    font-family: gillsans_light;
  }
  /deep/ p{
    font-size:16px;
    line-height:25px;
    font-family: gillsans_light;
  }
      // display:none;
      // transition:display 2s;
    }
  }
}
// .drop_down_item:hover{
//   .drop_down_content{
//     display:block;
//   }
// }


.cke_editable
{
	font-size: 13px;
	line-height: 1.6;

	/* Fix for missing scrollbars with RTL texts. (#10488) */
	word-wrap: break-word;
	font-family: gillsans_light;
}

blockquote
{
	font-style: italic;
	font-family: Georgia, Times, "Times New Roman", serif;
	padding: 2px 0;
	border-style: solid;
	border-color: #ccc;
	border-width: 0;
	font-family: gillsans_light;
}

.cke_contents_ltr blockquote
{
	padding-left: 20px;
	padding-right: 8px;
	border-left-width: 5px;
}

.cke_contents_rtl blockquote
{
	padding-left: 8px;
	padding-right: 20px;
	border-right-width: 5px;
}

a
{
	color: #0782C1;
}

ol,ul,dl
{
	/* IE7: reset rtl list margin. (#7334) */
	*margin-right: 0px;
	/* Preserved spaces for list items with text direction different than the list. (#6249,#8049)*/
	padding: 0 40px;
}

h1,h2,h3,h4,h5,h6
{
	font-weight: normal;
	line-height: 1.2;
}

hr
{
	border: 0px;
	border-top: 1px solid #ccc;
}

// p img{
//   text-align:center
// }
img{
  margin-left: auto; 
    margin-right:auto; 
    display:block;
}

img.right
{
	border: 1px solid #ccc;
	float: right;
	margin-left: 15px;
	padding: 5px;
}

img.left
{
	border: 1px solid #ccc;
	float: left;
	margin-right: 15px;
	padding: 5px;
}

pre
{
	white-space: pre-wrap; /* CSS 2.1 */
	word-wrap: break-word; /* IE7 */
	-moz-tab-size: 4;
	tab-size: 4;
}

.marker
{
	background-color: Yellow;
}


figure
{
	text-align: center;
	outline: solid 1px #ccc;
	background: rgba(0,0,0,0.05);
	padding: 10px;
	margin: 10px 20px;
	display: inline-block;
}

figure > figcaption
{
	text-align: center;
	display: block; /* For IE8 */
}

a > img {
	padding: 1px;
	margin: 1px;
	border: none;
	outline: 1px solid #0782C1;
}

/* Widget Styles */
.code-featured
{
	border: 5px solid red;
}

.math-featured
{
	padding: 20px;
	box-shadow: 0 0 2px rgba(200, 0, 0, 1);
	background-color: rgba(255, 0, 0, 0.05);
	margin: 10px;
}

.image-clean
{
	border: 0;
	background: none;
	padding: 0;
}

.image-clean > figcaption
{
	font-size: .9em;
	text-align: right;
}

.image-grayscale
{
	background-color: white;
	color: #666;
}

.image-grayscale img, img.image-grayscale
{
	filter: grayscale(100%);
}

.embed-240p
{
	max-width: 426px;
	max-height: 240px;
	margin:0 auto;
}

.embed-360p
{
	max-width: 640px;
	max-height: 360px;
	margin:0 auto;font-family: gillsans_light;
}

.embed-480p
{
	max-width: 854px;
	max-height: 480px;
	margin:0 auto;font-family: gillsans_light;
}

.embed-720p
{
	max-width: 1280px;
	max-height: 720px;
	margin:0 auto;font-family: gillsans_light;
}

.embed-1080p
{
	max-width: 1920px;
	max-height: 1080px;
	margin:0 auto;
	font-family: gillsans_light;
}


a{
  text-decoration: none;
  font-family: gillsans_light;
}
p{
	font-family: gillsans_light;
}

</style>