<template>
<div class="main">
    <div class="logo"></div>

    <div class="copyright_text">
        <br/>
        <br/>
        Let you know more about China.
    </div>
</div>
</template>


<script>
export default {
    methods:{
        change_route(path){
            this.$router.push("/" + path)
        }
    }
}
</script>


<style lang="less" scoped>
.main{
    background: rgb(59, 59, 59);
    height: 400px;
    padding-top:200px;
}
.logo{
    background: red;
    height: 80px;
    width: 230px;
    margin: 0 auto;
    
    background:url("../assets/logo.png") no-repeat center center;
}

.copyright_text{
    font-size: 14px;
    color: white;
    clear: both;
    width:300px;
    margin: 0 auto;
    text-align:center;
    transform: translate(3px,0px);
}
</style>>
