<template>
  <div v-bind:style="{background:color}" class="header">
        <div class="logo"></div>
        <div class="menu">

            <!-- <div class="nva_item">
                <div class="nav_tip"></div>
                <div class="nav_link">Home {{ $t('me')}}</div>
                <div class="nav_drop_down">
                    <div class="nav_drop_down_item">
                        <a href="#">你好</a>
                    </div>
                </div>
            </div> -->

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div @click="change_route('')"  class="nav_link">Home</div>
                <div class="nav_drop_down">

                </div>
            </div>

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div @click="change_route('about')" class="nav_link">About</div>
                <!-- <div class="nav_link">About</div> -->
                <div class="nav_drop_down">
                    
                </div>
            </div>

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div @click="change_route('programs')" class="nav_link">Program</div>
                <div class="nav_drop_down">
                    
                </div>
            </div>

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div @click="change_route('blogs')" class="nav_link">Blog</div>
                <!-- <div class="nav_link">Blogs</div> -->
                <div class="nav_drop_down">
                    
                </div>
            </div>

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div @click="change_route('contact')" class="nav_link">Contact</div>
                <div class="nav_drop_down">
                    
                </div>
            </div>

            <!-- <div class="nva_item nav_divider">
                <div class="nav_link">:</div>
            </div> -->

            <!-- <div class="nva_item">
                <div @click="change_lang" class="nav_link">中文</div>
            </div> -->

            <div class="nva_item">
                <div class="nav_tip"></div>
                <div class="nav_link nav_link_">{{ lang }}</div>
                <div class="nav_drop_down">
                    <div @click="change_lang('zh')" class="nav_drop_down_item">
                        <a >中文</a>
                        
                    </div>
                    <div @click="change_lang('en')" class="nav_drop_down_item">

                        <a >English</a>
                    </div>
                </div>
            </div>

            <div class="nva_item nva_buttom">
                <div @click="change_route('contact#enquire')" class="nav_link">ENQUIRE</div>
            </div>

        </div>
    </div>
</template>

<script>
export default {
        data(){
        return{
            'lang':'中文',
            'color':'#ffffff00'
        }
    },
    mounted (){
        let lang_c = localStorage.getItem('locale');
        if(lang_c == null){
            lang_c = 'zh'
        }
        let lang_str = '中文'
        if(lang_c == 'zh'){
            lang_str = "中文"
        }else if(lang_c == 'en'){
            lang_str = "English"
        }

        this.lang = lang_str;
        window.addEventListener('scroll', function() {
            let last_known_scroll_position = window.scrollY;
            // console.log(this.color);
            if(last_known_scroll_position == 0){
                // console.log("123")
                this.color = '#ffffff00'
            }else{
                this.color = '#000000b5'
                // console.log('#333030b5')
            }
        }.bind(this));
    },
    methods:{
        change_lang(lang_c){
            console.log(lang_c);
            localStorage.setItem('locale',lang_c);
            this.$i18n.locale = lang_c

            if(lang_c == null){
            lang_c = 'zh'
            }
            let lang_str = '中文'
            if(lang_c == 'zh'){
                lang_str = "中文"
            }else if(lang_c == 'en'){
                lang_str = "English"
            }

            this.lang = lang_str;
        },
        change_route(path){
            this.$router.push("/" + path)
        }
    }
}
</script>

<style lang="less" scoped>
.header{
    position: fixed;
    height: 80px;
    width:100%;
    // background: rgba(255, 0, 0, 0.445);
    padding-bottom:20px;
    
    // top:1px;
    z-index:100000;
}
.logo{
    background: red;
    height: 80px;
    width: 200px;
    float: left;
    margin-left: 100px; 
    margin-top: 16px; 
    background:url("../assets/logo.png") no-repeat center center;
}
.menu{
    // background: red;
    width: 930px;
    height: 100%;
    float: right;   
}
.nva_item{
    position: relative;
    // background: green;
    width: 11%;
    height: 100%;
    margin-right:10px;
    display: inline-block;
    .nav_tip{
        position: absolute;
        // background: red;
        height: 5px;
        width: 100%;
    }
    .nav_link{
        text-align: center;
        position: absolute;
        bottom: 10px;
        width: 100%;
        color: white;
        font-size: 20px;
        text-shadow: 5px 5px 8px #000000;

    }
    .nav_link_{
        font-size: 18px;
    }
    .nav_link:hover{
        cursor:pointer;
    }
    .nav_drop_down{
        margin-top: 80px;
        display: none;
        position: absolute;
        background: rgba(92, 92, 92, 0.404);
        // background:red;
        
        width: 200px;
        .nav_drop_down_item{
            padding: 10px 20px 10px 20px;
        }
        .nav_drop_down_item:hover{
            cursor:pointer;
            background: white;
            a{
                color: black;
            }
            
        }
        a{
            color: white;
            font-size: 20px;
        }
    }
}
.nva_item:hover{
    .nav_drop_down{
        display: block;
    }
    .nav_tip{
        background: rgb(187, 0, 0);
    }
}
.nav_divider{
    width: 20px;
    .nav_link:hover{
        cursor:default;
    }
}
.nva_buttom{
    // background: black;
    .nav_link{
        // padding: 5px;
        background: rgb(187, 0, 0);
        line-height: 30px;
        font-size: 16px;
        height: 30px;
        transform: translate(0px,5px);
    }
}

</style>
