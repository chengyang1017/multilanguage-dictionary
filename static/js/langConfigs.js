const langConfigs = {
        //1. 印欧
        //斯拉夫语族
        "ru": { name: "俄语", flag: "ru", title: "中俄词典" },
        "uk": { name: "乌克兰语", flag: "ua", title: "中乌克兰词典" },
        "be": { name: "白俄罗斯语", flag: "by", title: "中白俄词典" },
        "pl": { name: "波兰语", flag: "pl", title: "中波词典" },
        "cs": { name: "捷克语", flag: "cz", title: "中捷词典" },
        "bg": { name: "保加利亚语", flag: "bg", title: "中保词典" },
        "sr": { name: "塞尔维亚语", flag: "rs", title: "中塞词典" },
        "hr": { name: "克罗地亚语", flag: "hr", title: "中克词典" },
        "sk": { name: "斯洛伐克语", flag: "sk", title: "中斯洛词典" },
        "sl": { name: "斯洛文尼亚语", flag: "si", title: "中斯洛文尼亚词典" },
        "mk": { name: "马其顿语", flag: "mk", title: "中马其顿词典" },

        //罗曼语族
        "fr": { name: "法语", flag: "fr", title: "中法词典" },
        "es": { name: "西班牙语", flag: "es", title: "中西词典" },
        "it": { name: "意大利语", flag: "it", title: "中意词典" },
        "pt": { name: "葡萄牙语", flag: "pt", title: "中葡词典" },

        //日耳曼语族
        "de": { name: "德语", flag: "de", title: "中德词典" },
        "nl": { name: "荷兰语", flag: "nl", title: "中荷词典" },
        "sv": { name: "瑞典语", flag: "se", title: "中瑞词典" },
        "da": { name: "丹麦语", flag: "dk", title: "中丹词典" },
        "no": { name: "挪威语", flag: "no", title: "中挪词典" },
        "is": { name: "冰岛语", flag: "is", title: "中冰词典" },
        "fi": { name: "芬兰语", flag: "fi", title: "中芬词典" },

        //印度-伊朗语族
        "fa": { name: "波斯语", flag: "ir", title: "中波斯词典" },
        "hi": { name: "印地语", flag: "in", title: "中印地词典" },
        "bn": { name: "孟加拉语", flag: "bd", title: "中孟加拉词典" },
        "ur": { name: "乌尔都语", flag: "pk", title: "中乌尔都词典" },
        "tg": { name: "塔吉克语", flag: "tj", title: "中塔吉克词典" },

        //凯尔特语族
        "ga": { name: "爱尔兰语", flag: "ie", title: "中爱尔兰词典" },
        "cy": { name: "威尔士语", flag: "gb", title: "中威尔士词典" },

        //雅利安语族
        "mr": { name: "马拉地语", flag: "in", title: "中马拉地词典" },

        
        //2. 阿尔泰语系
        //突厥语族
        "tr": { name: "土耳其语", flag: "tr", title: "中土词典" },
        "kz": { name: "哈萨克语", flag: "kz", title: "中哈词典" },
        "ky": { name: "吉尔吉斯语", flag: "kg", title: "中吉词典" },
        "uz": { name: "乌兹别克语", flag: "uz", title: "中乌兹别克词典" },
        "tk": { name: "土库曼语", flag: "tm", title: "中土库曼词典" },
        "az": { name: "阿塞拜疆语", flag: "az", title: "中阿塞拜疆词典" },
        "tt": { name: "鞑靼语", flag: "ru", title: "中鞑靼词典" },
        "ug": { name: "维吾尔语", flag: "cn", title: "中维吾尔词典" },

        //汉藏语系
        //藏缅语族
        "bo": { name: "藏语", flag: "cn", title: "中藏词典" },
        "my": { name: "缅甸语", flag: "mm", title: "中缅词典" },
        
        //壮侗语族
        "th": { name: "泰语", flag: "th", title: "中泰词典" },
        "la": { name: "老挝语", flag: "la", title: "中老词典" },
        "": { name: "壮语", flag: "cn", title: "中壮词典" },

        //苗瑶语族
        "hmn": { name: "苗语", flag: "cn", title: "中苗词典" },

        //南亚语系
        //孟-高棉语族
        "vn": { name: "越南语", flag: "vn", title: "中越词典" },
        "km": { name: "高棉语", flag: "kh", title: "中柬词典" },

        //高加索语系
        "ce": { name: "车臣语", flag: "ru", title: "中车臣词典" },

        //南岛语系
        "id": { name: "印尼语", flag: "id", title: "中印尼词典" },
        "ms": { name: "马来语", flag: "my", title: "中马来词典" },
        "tl": { name: "菲律宾语", flag: "ph", title: "中菲词典" },
        "jv": { name: "爪哇语", flag: "id", title: "中爪哇词典" },

        //达罗毗荼语系
        "ta": { name: "泰米尔语", flag: "lk", title: "中泰米尔词典" },
        "te": { name: "泰卢固语", flag: "in", title: "中泰卢固词典" },
        "kn": { name: "卡纳达语", flag: "in", title : "中卡纳达词典" },
        "ml": { name: "马拉雅拉姆语", flag: "in", title: "中马拉雅拉姆词典" },
        "gu": { name: "古吉拉特语", flag: "in", title: "中古吉拉特词典" },

        "ko": { name: "韩语", flag: "kr", title: "中韩词典" },
        "ar": { name: "阿拉伯语", flag: "sa", title: "中阿词典" },
        "hu": { name: "匈牙利语", flag: "hu", title: "中匈词典" },
        "el": { name: "希腊语", flag: "gr", title: "中希词典" },
        "he": { name: "希伯来语", flag: "il", title: "中希伯来词典" },
        "ro": { name: "罗马尼亚语", flag: "ro", title: "中罗词典" },
        "lt": { name: "立陶宛语", flag: "lt", title: "中立词典" },
        "lv": { name: "拉脱维亚语", flag: "lv", title: "中拉词典" },
        "et": { name: "爱沙尼亚语", flag: "ee", title: "中爱词典" },


        "ka": { name: "格鲁吉亚语", flag: "ge", title: "中格词典" },
        "hy": { name: "亚美尼亚语", flag: "am", title: "中亚美尼亚词典" },
        "sq": { name: "阿尔巴尼亚语", flag: "al", title: "中阿尔巴尼亚词典" },
        "sw": { name: "斯瓦希里语", flag: "ke", title: "中斯瓦希里词典" },
        "am": { name: "阿姆哈拉语", flag: "et", title: "中阿姆哈拉词典" },
        "ha": { name: "豪萨语", flag: "ng", title: "中豪萨词典" },
        "zu": { name: "祖鲁语", flag: "za", title: "中祖鲁词典" },
        "mn": { name: "蒙古语", flag: "mn", title: "中蒙词典" },
        "qu": { name: "克丘亚语", flag: "pe", title: "中克丘亚词典" },
        "gn": { name: "瓜拉尼语", flag: "py", title: "中瓜拉尼词典" },
        "pa": { name: "旁遮普语", flag: "in", title: "中旁遮普词典" },
        "or": { name: "奥里亚语", flag: "in", title: "中奥里亚词典" },
        "si": { name: "僧伽罗语", flag: "lk", title: "中僧伽罗词典" },
        "os": { name: "奥塞梯语", flag: "ru", title: "中奥塞梯词典" },
        "ba": { name: "巴什基尔语", flag: "ru", title: "中巴什基尔词典" },
        "gag": { name: "加告兹语", flag: "md", title: "中加告兹词典" },
        "jp": { name: "日语", flag: "jp", title: "中日词典" }
    };