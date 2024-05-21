
    # template_data_new = {'SurveyElements': []}
    elems_list = []

    for element in template_data['SurveyElements']:
        if element['Element'] == 'SQ':
            if 'Payload' in element and 'QuestionText' in element['Payload']:
                question_text = element['Payload']['QuestionText']

                # Attempt to directly replace within the specific HTML format
                # <div id='scenario'>SCENARIO_TEXT<\/div>
                target_html = "<div id='scenario'>SCENARIO_TEXT</div>"
                replacement_html = f"<div id='scenario'>{scenario_text}</div>"
                if target_html in question_text:
                    element['Payload']['QuestionText'] = question_text.replace(target_html, replacement_html)
                    print("SCENARIO_TEXT replaced successfully.")
                    print(element['Payload']['QuestionText'])

                # Replace CHOICE_TEXT if present
                choice_target_html = "<div id='choice'>CHOICE_TEXT</div>"
                choice_replacement_html = f"<div id='choice'>{choice_text}</div>"
                if choice_target_html in question_text:
                    element['Payload']['QuestionText'] = question_text.replace(choice_target_html, choice_replacement_html)
                    print("CHOICE_TEXT replaced successfully.")

            # Update entities in choices
            if 'Choices' in element['Payload']:
                for entity_index, entity in enumerate(entities, start=1):
                    key = str(entity_index)
                    if key in element['Payload']['Choices']:
                        element['Payload']['Choices'][key]['Display'] = entity
                    else:
                        element['Payload']['Choices'][key] = {'Display': entity}

                # Remove excess entries
                current_keys = list(element['Payload']['Choices'].keys())
                for key in current_keys:
                    if int(key) > len(entities):
                        del element['Payload']['Choices'][key]
        
        elems_list.append(element)

    # template_data_new['SurveyElements'] = elems_list
    template_data['SurveyElements'] = elems_list

    return template_data
