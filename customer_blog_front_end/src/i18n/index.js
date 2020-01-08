import Vue from 'vue'
import VueI18n from 'vue-i18n'

import ZH from './lib/zh'
import EN from './lib/en'


Vue.use(VueI18n)

let lang_c = localStorage.getItem('locale');
if(lang_c == null){
    lang_c = 'en'
}

const i18n = new VueI18n({
  locale: lang_c,
  messages: {
    en: EN,
    zh: ZH
  }
})

export default i18n