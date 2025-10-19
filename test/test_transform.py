import pytest
from src.transform import transform


def test_transform_function_handles_empty_input_data():
    # Arrange
    input = []
    # Act
    result = transform(input)
    # Assert
    assert result == "No data to transform"

def test_transform_only_accepts_a_list_as_input_data_type():
    # Arrange
        # Arrange
    bad_inputs = ([1,2,3], 123, {1,2,3}, (1,2,3), True, None, "hello")
    # Act & Assert
    for input in bad_inputs:
        with pytest.raises(TypeError):    
            transform(input)

def test_transform_returns_a_list_of_dictionaries_when_passed_valid_list_with_one_record():
    # Arrange
    input = [{"id": "football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "type": "article", 
              "sectionId": "football", 
              "sectionName": "Football", 
              "webPublicationDate": "2025-09-06T21:22:38Z", 
              "webTitle": "World Cup qualifying roundup: Ronaldo scores twice as Portugal pay Jota tributes", 
              "webUrl": "https://www.theguardian.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "apiUrl": "https://content.guardianapis.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "fields": {"body": "<p>Cristiano Ronaldo scored his 139th and 140th international goals as <strong>Portugal</strong> thrashed <strong>Armenia</strong>  / 5-0 in their first match since the death of Diogo Jota in a car accident in July.</p> <p>A minute\u2019s silence was held before the World Cup qualifier <a href=\"https://www.theguardian.com/football/2025/jul/26/liverpool-diogo-jota-memorial-anfield\">in honour of Jota</a>, who won 49 caps for Portugal, and banners were on display around the Vazgen Sargsyan Republican Stadium in Yerevan.</p> <aside class=\"element element-rich-link element--thumbnail\"> <p> <span>Related: </span><a href=\"https://www.theguardian.com/football/2025/sep/06/uefa-has-last-chance-to-keep-genie-of-domestic-matches-abroad-in-its-bottle\">Uefa has last chance to keep genie of domestic matches abroad in its bottle</a> </p> </aside>  <p>Jo\u00e3o F\u00e9lix opened the scoring in the 10th minute before Ronaldo doubled their lead when he converted Pedro Neto\u2019s cross. Jo\u00e3o Cancelo celebrated his goal to make it 3-0 by mimicking Jota\u2019s video game celebration.</p> <p>The 40-year-old Ronaldo extended Portugal\u2019s lead to four shortly after half-time with a stunning strike of a bouncing ball from distance, while his Al-Nassr teammate F\u00e9lix added a second of his own to complete the scoring.</p>    <p>Adam Idah came off the bench to earn the <strong>Republic of Ireland</strong> a point from a dramatic 2-2 draw against 10-man <strong>Hungary</strong> in their opening qualifier.</p> <p>The Swansea striker\u2019s header in the third minute of injury time made it 2-2 after Ireland had fought their way back from 2-0 down to stave off defeat.</p> <p>Ireland\u2019s opening Group F fixture got off to a nightmare start when Barnabas Varga and Roland Sallai, who was later dismissed, scored inside the first 15 minutes.</p> <p>The Roma striker Evan Ferguson reduced the deficit from close range early in the second half and Sallai\u2019s premature departure, after a late challenge on Dara O\u2019Shea, left the technically more gifted Hungarians under siege.</p> <p>They almost managed to see out time but Idah intervened late on to keep Heimir Hallgrimsson\u2019s team on an even keel in the race for second place behind Portugal.</p> <p><strong>Serbia</strong> kept up their hopes of catching England in Group K with a 1-0 win against <strong>Latvia</strong> in Riga. Dusan Vlahovic scored the decisive goal in the 12th minute, slotting the ball past Krisjanis Zviedris from outside the penalty area.</p> <p>Dragan Stojkovic\u2019s side are five points behind the group leaders, England, with the two teams meeting in Belgrade on Tuesday.</p> <p>In the African section of World Cup qualifying, <strong>Nigeria</strong> live to fight another day after beating <strong>Rwanda</strong> 1-0. Tolu Arokodare, who completed a move from Genk to Wolves on transfer deadline day, scored an acrobatic 50th-minute winner after coming off the bench.</p> <p>Defeat for Nigeria in Uyo would have finished off their chances of qualifying for the World Cup but the victory moves them to within six points of the group leaders, South Africa, and five points behind second-place Benin with three games to go. Group winners qualify automatically for the finals in North America next summer, with second place heading into intercontinental playoffs.</p>"}, "isHosted": "false", "pillarId": "pillar/sport", "pillarName": "Sport"
            }]
       
    # Act
    result = transform(input)
    # Assert
    assert isinstance(result, list)
    assert isinstance(result[0], dict)

def test_transform_returns_a_list_of_dictionaries_when_passed_valid_list_with_multiple_records():
    # Arrange
    input = [{  "id": "football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
                "type": "article", 
                "sectionId": "football", 
                "sectionName": "Football", 
                "webPublicationDate": "2025-09-06T21:22:38Z", 
                "webTitle": "Number 1", 
                "webUrl": "https://www.theguardian.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
                "apiUrl": "https://content.guardianapis.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
                "fields": {"body": "<p>Cristiano Ronaldo scored his 139th and 140th international goals as <strong>Portugal</strong> thrashed <strong>Armenia</strong>  / 5-0 in their first match since the death of Diogo Jota in a car accident in July.</p> <p>A minute\u2019s silence was held before the World Cup qualifier <a href=\"https://www.theguardian.com/football/2025/jul/26/liverpool-diogo-jota-memorial-anfield\">in honour of Jota</a>, who won 49 caps for Portugal, and banners were on display around the Vazgen Sargsyan Republican Stadium in Yerevan.</p> <aside class=\"element element-rich-link element--thumbnail\"> <p> <span>Related: </span><a href=\"https://www.theguardian.com/football/2025/sep/06/uefa-has-last-chance-to-keep-genie-of-domestic-matches-abroad-in-its-bottle\">Uefa has last chance to keep genie of domestic matches abroad in its bottle</a> </p> </aside>  <p>Jo\u00e3o F\u00e9lix opened the scoring in the 10th minute before Ronaldo doubled their lead when he converted Pedro Neto\u2019s cross. Jo\u00e3o Cancelo celebrated his goal to make it 3-0 by mimicking Jota\u2019s video game celebration.</p> <p>The 40-year-old Ronaldo extended Portugal\u2019s lead to four shortly after half-time with a stunning strike of a bouncing ball from distance, while his Al-Nassr teammate F\u00e9lix added a second of his own to complete the scoring.</p>    <p>Adam Idah came off the bench to earn the <strong>Republic of Ireland</strong> a point from a dramatic 2-2 draw against 10-man <strong>Hungary</strong> in their opening qualifier.</p> <p>The Swansea striker\u2019s header in the third minute of injury time made it 2-2 after Ireland had fought their way back from 2-0 down to stave off defeat.</p> <p>Ireland\u2019s opening Group F fixture got off to a nightmare start when Barnabas Varga and Roland Sallai, who was later dismissed, scored inside the first 15 minutes.</p> <p>The Roma striker Evan Ferguson reduced the deficit from close range early in the second half and Sallai\u2019s premature departure, after a late challenge on Dara O\u2019Shea, left the technically more gifted Hungarians under siege.</p> <p>They almost managed to see out time but Idah intervened late on to keep Heimir Hallgrimsson\u2019s team on an even keel in the race for second place behind Portugal.</p> <p><strong>Serbia</strong> kept up their hopes of catching England in Group K with a 1-0 win against <strong>Latvia</strong> in Riga. Dusan Vlahovic scored the decisive goal in the 12th minute, slotting the ball past Krisjanis Zviedris from outside the penalty area.</p> <p>Dragan Stojkovic\u2019s side are five points behind the group leaders, England, with the two teams meeting in Belgrade on Tuesday.</p> <p>In the African section of World Cup qualifying, <strong>Nigeria</strong> live to fight another day after beating <strong>Rwanda</strong> 1-0. Tolu Arokodare, who completed a move from Genk to Wolves on transfer deadline day, scored an acrobatic 50th-minute winner after coming off the bench.</p> <p>Defeat for Nigeria in Uyo would have finished off their chances of qualifying for the World Cup but the victory moves them to within six points of the group leaders, South Africa, and five points behind second-place Benin with three games to go. Group winners qualify automatically for the finals in North America next summer, with second place heading into intercontinental playoffs.</p>"
                            }, 
                            "isHosted": "false", 
                            "pillarId": "pillar/sport", 
                            "pillarName": "Sport"
            },
            {
                "id": "football/2025/oct/13/world-cup-qualifying-roundup-sweden-on-brink-of-elimination-after-kosovo-defeat",
                "type": "article",
                "sectionId": "football",
                "sectionName": "Football",
                "webPublicationDate": "2025-10-13T17:59:00Z",
                "webTitle": "Number 2",
                "webUrl": "https://www.theguardian.com/football/2025/oct/13/world-cup-qualifying-roundup-sweden-on-brink-of-elimination-after-kosovo-defeat",
                "apiUrl": "https://content.guardianapis.com/football/2025/oct/13/world-cup-qualifying-roundup-sweden-on-brink-of-elimination-after-kosovo-defeat",
                "fields": {"body": "<p>Sweden hopes of reaching the 2026 World Cup took a serious hit after a 1-0 home defeat by Kosovo, who claimed a landmark victory. France were held 2-2 by Iceland as the European qualifiers intensified.</p>"
                            },
                            "isHosted": "false",
                            "pillarId": "pillar/sport",
                            "pillarName": "Sport"
                }
            ]
       
    # Act
    result = transform(input)
    # Assert
    assert len(result) == 2
    assert result[0]['webTitle'] == 'Number 1'
    assert result[1]['webTitle'] == 'Number 2'

def test_transform_returns_a_four_key_value_pairs_when_passed_valid_input_data():
    # Arrange
    input = [{"id": "football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "type": "article", 
              "sectionId": "football", 
              "sectionName": "Football", 
              "webPublicationDate": "2025-09-06T21:22:38Z", 
              "webTitle": "World Cup qualifying roundup: Ronaldo scores twice as Portugal pay Jota tributes", 
              "webUrl": "https://www.theguardian.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "apiUrl": "https://content.guardianapis.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "fields": {"body": "<p>Cristiano Ronaldo scored his 139th and 140th international goals as <strong>Portugal</strong> thrashed <strong>Armenia</strong>  / 5-0 in their first match since the death of Diogo Jota in a car accident in July.</p> <p>A minute\u2019s silence was held before the World Cup qualifier <a href=\"https://www.theguardian.com/football/2025/jul/26/liverpool-diogo-jota-memorial-anfield\">in honour of Jota</a>, who won 49 caps for Portugal, and banners were on display around the Vazgen Sargsyan Republican Stadium in Yerevan.</p> <aside class=\"element element-rich-link element--thumbnail\"> <p> <span>Related: </span><a href=\"https://www.theguardian.com/football/2025/sep/06/uefa-has-last-chance-to-keep-genie-of-domestic-matches-abroad-in-its-bottle\">Uefa has last chance to keep genie of domestic matches abroad in its bottle</a> </p> </aside>  <p>Jo\u00e3o F\u00e9lix opened the scoring in the 10th minute before Ronaldo doubled their lead when he converted Pedro Neto\u2019s cross. Jo\u00e3o Cancelo celebrated his goal to make it 3-0 by mimicking Jota\u2019s video game celebration.</p> <p>The 40-year-old Ronaldo extended Portugal\u2019s lead to four shortly after half-time with a stunning strike of a bouncing ball from distance, while his Al-Nassr teammate F\u00e9lix added a second of his own to complete the scoring.</p>    <p>Adam Idah came off the bench to earn the <strong>Republic of Ireland</strong> a point from a dramatic 2-2 draw against 10-man <strong>Hungary</strong> in their opening qualifier.</p> <p>The Swansea striker\u2019s header in the third minute of injury time made it 2-2 after Ireland had fought their way back from 2-0 down to stave off defeat.</p> <p>Ireland\u2019s opening Group F fixture got off to a nightmare start when Barnabas Varga and Roland Sallai, who was later dismissed, scored inside the first 15 minutes.</p> <p>The Roma striker Evan Ferguson reduced the deficit from close range early in the second half and Sallai\u2019s premature departure, after a late challenge on Dara O\u2019Shea, left the technically more gifted Hungarians under siege.</p> <p>They almost managed to see out time but Idah intervened late on to keep Heimir Hallgrimsson\u2019s team on an even keel in the race for second place behind Portugal.</p> <p><strong>Serbia</strong> kept up their hopes of catching England in Group K with a 1-0 win against <strong>Latvia</strong> in Riga. Dusan Vlahovic scored the decisive goal in the 12th minute, slotting the ball past Krisjanis Zviedris from outside the penalty area.</p> <p>Dragan Stojkovic\u2019s side are five points behind the group leaders, England, with the two teams meeting in Belgrade on Tuesday.</p> <p>In the African section of World Cup qualifying, <strong>Nigeria</strong> live to fight another day after beating <strong>Rwanda</strong> 1-0. Tolu Arokodare, who completed a move from Genk to Wolves on transfer deadline day, scored an acrobatic 50th-minute winner after coming off the bench.</p> <p>Defeat for Nigeria in Uyo would have finished off their chances of qualifying for the World Cup but the victory moves them to within six points of the group leaders, South Africa, and five points behind second-place Benin with three games to go. Group winners qualify automatically for the finals in North America next summer, with second place heading into intercontinental playoffs.</p>"}, "isHosted": "false", "pillarId": "pillar/sport", "pillarName": "Sport"
            }]
    
    expected_keys = {"webPublicationDate", "webTitle","webUrl", "content_preview"}
    
    # Act
    result = transform(input)
    # Assert
    assert len(result[0].keys()) == 4 
    assert  set(result[0].keys()) == expected_keys 

def test_transform_returns_1000_or_less_characters_for_the_content_preview_field():
    # Arrange
    input = [{"id": "football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "type": "article", 
              "sectionId": "football", 
              "sectionName": "Football", 
              "webPublicationDate": "2025-09-06T21:22:38Z", 
              "webTitle": "World Cup qualifying roundup: Ronaldo scores twice as Portugal pay Jota tributes", 
              "webUrl": "https://www.theguardian.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "apiUrl": "https://content.guardianapis.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "fields": {"body": "<p>Cristiano Ronaldo scored his 139th and 140th international goals as <strong>Portugal</strong> thrashed <strong>Armenia</strong>  / 5-0 in their first match since the death of Diogo Jota in a car accident in July.</p> <p>A minute\u2019s silence was held before the World Cup qualifier <a href=\"https://www.theguardian.com/football/2025/jul/26/liverpool-diogo-jota-memorial-anfield\">in honour of Jota</a>, who won 49 caps for Portugal, and banners were on display around the Vazgen Sargsyan Republican Stadium in Yerevan.</p> <aside class=\"element element-rich-link element--thumbnail\"> <p> <span>Related: </span><a href=\"https://www.theguardian.com/football/2025/sep/06/uefa-has-last-chance-to-keep-genie-of-domestic-matches-abroad-in-its-bottle\">Uefa has last chance to keep genie of domestic matches abroad in its bottle</a> </p> </aside>  <p>Jo\u00e3o F\u00e9lix opened the scoring in the 10th minute before Ronaldo doubled their lead when he converted Pedro Neto\u2019s cross. Jo\u00e3o Cancelo celebrated his goal to make it 3-0 by mimicking Jota\u2019s video game celebration.</p> <p>The 40-year-old Ronaldo extended Portugal\u2019s lead to four shortly after half-time with a stunning strike of a bouncing ball from distance, while his Al-Nassr teammate F\u00e9lix added a second of his own to complete the scoring.</p>    <p>Adam Idah came off the bench to earn the <strong>Republic of Ireland</strong> a point from a dramatic 2-2 draw against 10-man <strong>Hungary</strong> in their opening qualifier.</p> <p>The Swansea striker\u2019s header in the third minute of injury time made it 2-2 after Ireland had fought their way back from 2-0 down to stave off defeat.</p> <p>Ireland\u2019s opening Group F fixture got off to a nightmare start when Barnabas Varga and Roland Sallai, who was later dismissed, scored inside the first 15 minutes.</p> <p>The Roma striker Evan Ferguson reduced the deficit from close range early in the second half and Sallai\u2019s premature departure, after a late challenge on Dara O\u2019Shea, left the technically more gifted Hungarians under siege.</p> <p>They almost managed to see out time but Idah intervened late on to keep Heimir Hallgrimsson\u2019s team on an even keel in the race for second place behind Portugal.</p> <p><strong>Serbia</strong> kept up their hopes of catching England in Group K with a 1-0 win against <strong>Latvia</strong> in Riga. Dusan Vlahovic scored the decisive goal in the 12th minute, slotting the ball past Krisjanis Zviedris from outside the penalty area.</p> <p>Dragan Stojkovic\u2019s side are five points behind the group leaders, England, with the two teams meeting in Belgrade on Tuesday.</p> <p>In the African section of World Cup qualifying, <strong>Nigeria</strong> live to fight another day after beating <strong>Rwanda</strong> 1-0. Tolu Arokodare, who completed a move from Genk to Wolves on transfer deadline day, scored an acrobatic 50th-minute winner after coming off the bench.</p> <p>Defeat for Nigeria in Uyo would have finished off their chances of qualifying for the World Cup but the victory moves them to within six points of the group leaders, South Africa, and five points behind second-place Benin with three games to go. Group winners qualify automatically for the finals in North America next summer, with second place heading into intercontinental playoffs.</p>"}, "isHosted": "false", "pillarId": "pillar/sport", "pillarName": "Sport"
            }]
    
    # Act
    result = transform(input)
    # Assert
    assert  len(result[0]["content_preview"]) <= 1000

def test_creates_a_new_object():
    # Arrange
    input = [{"id": "football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "type": "article", 
              "sectionId": "football", 
              "sectionName": "Football", 
              "webPublicationDate": "2025-09-06T21:22:38Z", 
              "webTitle": "World Cup qualifying roundup: Ronaldo scores twice as Portugal pay Jota tributes", 
              "webUrl": "https://www.theguardian.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "apiUrl": "https://content.guardianapis.com/football/2025/sep/06/world-cup-qualifying-roundup-ronaldo-scores-twice-as-portugal-pay-jota-tributes", 
              "fields": {"body": "<p>Cristiano Ronaldo scored his 139th and 140th international goals as <strong>Portugal</strong> thrashed <strong>Armenia</strong>  / 5-0 in their first match since the death of Diogo Jota in a car accident in July.</p> <p>A minute\u2019s silence was held before the World Cup qualifier <a href=\"https://www.theguardian.com/football/2025/jul/26/liverpool-diogo-jota-memorial-anfield\">in honour of Jota</a>, who won 49 caps for Portugal, and banners were on display around the Vazgen Sargsyan Republican Stadium in Yerevan.</p> <aside class=\"element element-rich-link element--thumbnail\"> <p> <span>Related: </span><a href=\"https://www.theguardian.com/football/2025/sep/06/uefa-has-last-chance-to-keep-genie-of-domestic-matches-abroad-in-its-bottle\">Uefa has last chance to keep genie of domestic matches abroad in its bottle</a> </p> </aside>  <p>Jo\u00e3o F\u00e9lix opened the scoring in the 10th minute before Ronaldo doubled their lead when he converted Pedro Neto\u2019s cross. Jo\u00e3o Cancelo celebrated his goal to make it 3-0 by mimicking Jota\u2019s video game celebration.</p> <p>The 40-year-old Ronaldo extended Portugal\u2019s lead to four shortly after half-time with a stunning strike of a bouncing ball from distance, while his Al-Nassr teammate F\u00e9lix added a second of his own to complete the scoring.</p>    <p>Adam Idah came off the bench to earn the <strong>Republic of Ireland</strong> a point from a dramatic 2-2 draw against 10-man <strong>Hungary</strong> in their opening qualifier.</p> <p>The Swansea striker\u2019s header in the third minute of injury time made it 2-2 after Ireland had fought their way back from 2-0 down to stave off defeat.</p> <p>Ireland\u2019s opening Group F fixture got off to a nightmare start when Barnabas Varga and Roland Sallai, who was later dismissed, scored inside the first 15 minutes.</p> <p>The Roma striker Evan Ferguson reduced the deficit from close range early in the second half and Sallai\u2019s premature departure, after a late challenge on Dara O\u2019Shea, left the technically more gifted Hungarians under siege.</p> <p>They almost managed to see out time but Idah intervened late on to keep Heimir Hallgrimsson\u2019s team on an even keel in the race for second place behind Portugal.</p> <p><strong>Serbia</strong> kept up their hopes of catching England in Group K with a 1-0 win against <strong>Latvia</strong> in Riga. Dusan Vlahovic scored the decisive goal in the 12th minute, slotting the ball past Krisjanis Zviedris from outside the penalty area.</p> <p>Dragan Stojkovic\u2019s side are five points behind the group leaders, England, with the two teams meeting in Belgrade on Tuesday.</p> <p>In the African section of World Cup qualifying, <strong>Nigeria</strong> live to fight another day after beating <strong>Rwanda</strong> 1-0. Tolu Arokodare, who completed a move from Genk to Wolves on transfer deadline day, scored an acrobatic 50th-minute winner after coming off the bench.</p> <p>Defeat for Nigeria in Uyo would have finished off their chances of qualifying for the World Cup but the victory moves them to within six points of the group leaders, South Africa, and five points behind second-place Benin with three games to go. Group winners qualify automatically for the finals in North America next summer, with second place heading into intercontinental playoffs.</p>"}, "isHosted": "false", "pillarId": "pillar/sport", "pillarName": "Sport"
            }]
    
    # Act
    result = transform(input)
    # Assert
    assert  result is not input

