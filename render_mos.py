#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment

NUM = 10

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")  # 使用mos.html.jinja2和base.html.jinja2

    html = template.render(
        page_title = "音乐生成结果评测",
        # 原来的
        # form_url="https://script.google.com/macros/s/AKfycbzApm3cSoTRMbhTaEgd3c3VtpV9nRP1DUqxXQLsyVz9uAtTrSty/exec",
        form_url = "https://script.google.com/macros/s/AKfycbz004_N4jbOiaE0DBxqdC6rK5E2rJEo_570_NTU5VXgyHD5TdKODXzwbl8Dj5ii_Jm3nQ/exec",
        # form_id = 1,
        # 总共NUM_x个问题
        # question1图灵测试单个音频[1,5)，
        # questions2单个音频打分3道题[5,8)，
        # questions3比较两个音频3道题[8,NUM+1)
        questions1 = [{
                    "title" : "Question " + str(i),
                    "audio_paths":  ["audios/q"+str(i)+"/test1.wav"],
                    "name": "q" + str(i)
                    } 
                    for i in range(1,5)
                    ],
        questions2 = [{
                    "title" : "Question " + str(i),
                    "audio_paths":  ["audios/q"+str(i)+"/test1.wav"],
                    "name": "q" + str(i)
                    } 
                    for i in range(5,8)
                    ],
        questions3 = [{
                    "title" : "Question " + str(i),
                    "audio_paths":  ["audios/q"+str(i)+"/test1.wav","audios/q"+str(i)+"/test2.wav"],
                    "name": "q" + str(i)
                    } 
                    for i in range(8,NUM+1)
                    ]
        
    )
    with open("rendered_mos_v2.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
