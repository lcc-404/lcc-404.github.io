#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment

NUM = 3

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")  # 使用mos.html.jinja2和base.html.jinja2

    html = template.render(
        page_title="音乐生成结果评测",
        # 原来的
        # form_url="https://script.google.com/macros/s/AKfycbzApm3cSoTRMbhTaEgd3c3VtpV9nRP1DUqxXQLsyVz9uAtTrSty/exec",
        form_url="https://script.google.com/macros/s/AKfycbyChyf_QXTnHlCxov3oVmNigd3uz_jd4gJ1ZOiaNm5PhMRYK2K9W2WS_nIckZDFfmJRcg/exec",
        form_id=1,
        # 总共NUM=3个问题，每个问题2个选项
        questions=[{
                    "title" : "Question " + str(i),
                    "audio_paths": ["wavs/q"+str(i)+"/test1.wav",
                                    "wavs/q"+str(i)+"/test2.wav"],
                    "name": "q" + str(i)
                    } 
                    for i in range(1,NUM+1)
                    ]
    )
    with open("rendered_mos_v2.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
