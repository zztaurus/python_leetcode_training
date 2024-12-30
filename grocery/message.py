header_blocks = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "今日份题目已送达！"
        }
    }
]

question_blocks = [
        {
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:one: 展示题目样式，凑字数专用文字？*\nA. 素材的节奏速度\nB. 素材的节奏速度\nC. 整体画面饱和度\nD. 素材的人物数量"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "A",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "B",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "C",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "D",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-3"
				}
			]
		}
]

correct_quetion_blocks = [
    {
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:two: 回答正确样式，凑字数专用文字？*\nA. 素材的节奏速度\nB. 素材的节奏速度\nC. 整体画面饱和度\nD. 素材的人物数量"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":white_check_mark:，答案： *A* \n*认知：* 卖惨素材，整个画面调整整体画面饱和度明亮些，相比较暗画面素材cpi便宜10%。"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":please: *答完请随手给每道题来个“速评”*"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:题目待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		}
]

wrong_quetion_blocks = [
    {
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:three:回答错误样式，凑字数专用文字？*\nA. 素材的节奏速度\nB. 素材的节奏速度\nC. 整体画面饱和度\nD. 素材的人物数量"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":x:，答案： *A* \n\n*认知：* 卖惨素材，整个画面调整整体画面饱和度明亮些，相比较暗画面素材cpi便宜10%。"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":please: *答完请随手给每道题来个“速评”*"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:题目待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:认知超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:认知还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:认知待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		}
]

blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "今日份题目已送达！"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:one: 展示题目样式，凑字数专用文字？*\nA. 素材的节奏速度\nB. 素材的节奏速度\nC. 整体画面饱和度\nD. 素材的人物数量"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "A",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "B",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "C",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "D",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-3"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:two: 回答正确样式，凑字数专用文字？*\nA. 素材的节奏速度\nB. 素材的节奏速度\nC. 整体画面饱和度\nD. 素材的人物数量"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":white_check_mark:，答案： *A* \n*认知：* 卖惨素材，整个画面调整整体画面饱和度明亮些，相比较暗画面素材cpi便宜10%。"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":please: *答完请随手给每道题来个“速评”*"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:题目待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:认知超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:认知还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:认知待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:three:回答错误样式，凑字数专用文字？*\nA. 素材的节奏速度\nB. 素材的节奏速度\nC. 整体画面饱和度\nD. 素材的人物数量"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":x:，答案： *A* \n\n*认知：* 卖惨素材，整个画面调整整体画面饱和度明亮些，相比较暗画面素材cpi便宜10%。"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":please: *答完请随手给每道题来个“速评”*"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:题目待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:认知超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:认知还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:认知待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:four: 问卷反馈样式，凑字数专用文字？*\nA. 素材的节奏速度\nB. 素材的节奏速度\nC. 整体画面饱和度\nD. 素材的人物数量"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":white_check_mark:，答案： *A* \n*认知：* 卖惨素材，整个画面调整整体画面饱和度明亮些，相比较暗画面素材cpi便宜10%。"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": ":bixin:",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:five: 凑字数专用文字，凑字数专用文字凑字数专用文字凑字数专用文字？*\nA. 素材的节奏速度\nB. 素材的节奏速度\nC. 整体画面饱和度\nD. 素材的人物数量"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "A",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "B",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "C",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "D",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-3"
				}
			]
		},
		{
			"type": "divider"
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"placeholder": {
					"type": "plain_text",
					"text": "请填写“_”处的内容，多个填写项请用“；”分隔。",
					"emoji": True
				},
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": ":six: 三消排版不扣分的三个关键词是：__、___、__",
				"emoji": True
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "提交",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*:six: 填空题答案样式，三消排版不扣分的三个关键词是：__、___、__*"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":white_check_mark:，答案： *简洁；平衡感；对齐* \n\n *认知：* 三消排版的6个关键词：\n不扣分的三个关键词：简洁、平衡感、对齐\n有加分的三个关键词：氛围感、节奏感、恰到好处的装饰"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":please: *答完请随手给每道题来个“速评”*"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:题目还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:题目待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:认知超赞！",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-0"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":+1:认知还行",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-1"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": ":-1:认知待改进",
						"emoji": True
					},
					"value": "click_me_123",
					"action_id": "actionId-2"
				}
			]
		}
	]
