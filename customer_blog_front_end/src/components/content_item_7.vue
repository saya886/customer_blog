<template>
<div class="main">
    <div class="logo"></div>
    <dir class="menu">
        <div class="menu_item">Home</div>
        <div class="menu_item">About</div>
        <div class="menu_item">Programs</div>
        <div class="menu_item">Blogs</div>
        <div class="menu_item">Contact</div>
        <div class="menu_item menu_item_1">中文</div>
    </dir>
    <div class="copyright_text">
        <br/>
        <br/>
        © 2019 CURATEDCHINA<br/>
        <br/>沪ICP证190815号 
    </div>
</div>
</template>

<script>
export default {

}
</script>

<style lang="less" scoped>
.main{
    background: rgb(59, 59, 59);
    height: 400px;
}
.logo{
    background: red;
    height: 80px;
    width: 230px;
    float: left;
    margin-left: 120px; 
    margin-top: 50px;
    background:url("../assets/logo.png") no-repeat center center;
}
.menu{
    // width: 70%;
    margin-top: 98px;
    float: right;
    .menu_item{
        display: inline-block;
        font-size: 20px;
        
        margin-right:50px;
        color: white;
    }
    .menu_item_1{
        margin-left: 150px;
        margin-right: 150px;
    }
}
.copyright_text{
    font-size: 14px;
    color: white;
    clear: both;
    margin-left: 150px; 
    
}
</style>>
