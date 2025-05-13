1. ##### 本软件用于生成 '农场AI助手'中 "_internal/script"文件夹内的"脚本文本"


   1) 步骤解析原理: 星宝前进的全部步骤的集合为一个tuple, 这个tuple中包含的每一小步骤为dict类型. 程序解析每一小步骤dict, 生成对应的动作.*例如: 无人机v2  = ( {    },{   },{   },... )*
   2) 自定义的tuple经PyYAML包的函数dump()为yaml文件.
   3) 当然如果熟悉yaml格式, 也可以一步到位, **直接在原始yaml文件上修改**, 效果是一样的.
2. ##### **环境和依赖**

   本文件生成的脚本文件用于'农场AI助手'的版本号>"1.7.0"

   Python3.13
   PyYAML
3. ##### 文件说明:

   action_define: 该文件夹包含定义各脚本的数据.

   --action_animal: 非月卡牧场

   --action_base: 基础按键.

   --action_farmland_65: 非月卡农场.

   --action_catch_fish: 炸鱼

   --action_fishpond: 非月卡鱼塘

   --action_general:  无人机/开鱼塘/收鱼缸/泡温泉/喝咖啡/许愿金币/许愿经验/投喂小狗/摸小狗

   --action_processor: 非月卡加工器

   script: 该文件夹包含生成的yaml文件

   main.py: 入口程序.
4. ##### 步骤定义说明:

   每个dict的定义, 请参照以下已列出的条目.

   step: 自定义步骤名称, **任何名称均可**.

   type: 分为鼠标(mouse), 键盘(key/up/down), 延迟(sleep)三类.

   ###### a. 鼠标.


   1) 鼠标左键点击:

      ```
      {
      "step": "点击",
      "type": "mouse",
      "input": "click",
      "point": (960, 512),
      }
      ```

      > *注意: point的坐标可自定义.*
      >
   2) 鼠标左键按下:

      ```
      {
      "step": "拉动视角2",
      "type": "mouse",
      "input": "down",
      "point": None,
      },
      ```

      > *注意: point为None.*
      >
   3) 鼠标左键松开:

      ```
      {
         "step": "拉动视角4",
         "type": "mouse",
         "input": "up",
         "point": None,
         }
      ```

      > *注意: point为None.*
      >
   4) 鼠标左键移动:

      ```
      {
      "step": "拉动视角1",
      "type": "mouse",
      "input": "move",
      "point": (504, 280),
      }
      ```

      > *注意: point的坐标可自定义.*
      >

   ###### b.  键盘按键.

   1) 按键点击:
      ``   { "step": "Q键位置", "type": "key", "input": "Q", "delay": None, }``

      > *注意: type为key, "delay"的值为None或者数值, **单位ms**, 表示该按键按住多长时间.*
      >
   2) 按键按下:

      ``{ "step": "移动到无人机旁", "type": "down",  "input": "A",    "delay": None,}   ``

      > *注意: type为down, delay为None. 执行该命令后, 按键为按下状态, 直到"按键松开". 可与"延迟" "鼠标"等组合, 模拟多键同时按下的效果.*
      >
   3) 按键松开:

      ``{ "step": "移动到无人机旁",  "type": "up",   "input": "A",  "delay": None,    },   ``

      > *注意: type为up, delay为None*
      >

   ###### c. 延迟.

   ``{   "step": "延迟",   "type": "sleep",   "time": 1,   }``

   > *注意: time的单位为s*
   >

---

5. ##### 替换:

   当app"停止脚本"时, 使用新生成的yaml替换"script"文件夹内的原文件, 文件名保持一致, 点击"启动脚本"将运行新文件.
6. ##### 捕捉农场坐标的方法:

   1. 截图方式:
      点击"农场AI助手"中的"3.请确认已登录农场", 会在app的文件夹中生成'example'的图片, 用图像查看软件可以观察坐标位置, 比如鼠标移到图像的左上角,坐标为(0,0), 右下角坐标为(1008,568)
         
   2. javascript方式:
      在浏览器的console中, 使用javascript代码捕捉坐标位置. 适合熟悉javascript的星宝.

---
