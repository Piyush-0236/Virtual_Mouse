import util

def is_left_click(thumb_finger_dist,landmarks_list):
    thumb_index_top_dist = util.get_distance((landmarks_list[4],landmarks_list[8]))
    return (util.get_angle(landmarks_list[9],landmarks_list[10],landmarks_list[12]) > 90 and
            util.get_angle(landmarks_list[13],landmarks_list[14],landmarks_list[16]) < 50 and
            util.get_angle(landmarks_list[17],landmarks_list[18],landmarks_list[20]) < 50 and
            thumb_index_top_dist < 35 and
            thumb_finger_dist > 20)

def is_right_click(thumb_finger_dist,landmarks_list):
    thumb_middle_dist = util.get_distance((landmarks_list[4],landmarks_list[12]))
    return (util.get_angle(landmarks_list[5],landmarks_list[6],landmarks_list[8]) > 90 and
            util.get_angle(landmarks_list[13],landmarks_list[14],landmarks_list[16]) < 50 and
            util.get_angle(landmarks_list[17],landmarks_list[18],landmarks_list[20]) < 50 and
            thumb_middle_dist < 35 and
            thumb_finger_dist > 20)

def is_double_click(thumb_finger_dist,landmarks_list):
    index_middle_dist = util.get_distance((landmarks_list[8],landmarks_list[12]))
    thumb_index_middle_dist = util.get_distance((landmarks_list[4],landmarks_list[6]))
    return (util.get_angle(landmarks_list[5],landmarks_list[6],landmarks_list[8]) > 90 and
            util.get_angle(landmarks_list[9],landmarks_list[10],landmarks_list[12]) > 90 and
            thumb_index_middle_dist < 35 and
            index_middle_dist < 35 and
            thumb_finger_dist > 20)

def is_destroy(thumb_finger_dist,landmarks_list):
    middle_wrist_dist = util.get_distance((landmarks_list[0],landmarks_list[12]))
    return (middle_wrist_dist < 95 and thumb_finger_dist > 20)

def is_minimize(thumb_finger_dist,landmarks_list):
    index_middle_dist = util.get_distance((landmarks_list[8],landmarks_list[12]))
    thumb_ring_middle_dist = util.get_distance((landmarks_list[4],landmarks_list[14]))
    return (util.get_angle(landmarks_list[5],landmarks_list[6],landmarks_list[8]) > 90 and
            util.get_angle(landmarks_list[9],landmarks_list[10],landmarks_list[12]) > 90 and
            index_middle_dist < 35 and
            thumb_ring_middle_dist < 35 and
            thumb_finger_dist > 20 )


def all_windows(landmarks_list):
    thumb_index_dist = util.get_distance((landmarks_list[4],landmarks_list[8]))
    thumb_middle_dist = util.get_distance((landmarks_list[4],landmarks_list[12]))
    thumb_ring_dist = util.get_distance((landmarks_list[4],landmarks_list[16]))
    thumb_pinki_dist = util.get_distance((landmarks_list[4],landmarks_list[20]))

    return (thumb_index_dist < 35 and
            thumb_middle_dist < 35 and
            thumb_ring_dist < 35 and
            thumb_pinki_dist < 35)

def sound_down(landmarks_list):
    thumb_finger_dist  = util.get_distance((landmarks_list[4],landmarks_list[8]))
    thumb_pinki_dist = util.get_distance((landmarks_list[4],landmarks_list[20]))
    return (thumb_pinki_dist > 10 and thumb_pinki_dist < 30 and thumb_finger_dist > 100)

def sound_up(landmarks_list):
    thumb_finger_dist  = util.get_distance((landmarks_list[4],landmarks_list[8]))
    thumb_pinki_dist = util.get_distance((landmarks_list[4],landmarks_list[20]))
    return (thumb_pinki_dist > 30 and thumb_pinki_dist < 60 and thumb_finger_dist > 100)