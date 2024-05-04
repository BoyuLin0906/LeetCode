/*
Runtime 1 ms / Beats 78.69%
Memory 2.22 MB / Beats 19.67%
*/

func compareVersion(version1 string, version2 string) int {

    v1_slice := strings.Split(version1, ".")
    v2_slice := strings.Split(version2, ".")

    for len(v1_slice) > 0 && len(v2_slice) > 0 {

        v1_num, _ := strconv.Atoi(v1_slice[0])
        v2_num, _ := strconv.Atoi(v2_slice[0])
        if v1_num > v2_num {
            return 1
        } else if v2_num > v1_num {
            return -1
        }
        v1_slice = v1_slice[1:]
        v2_slice = v2_slice[1:]
    }

    for len(v1_slice) > 0 {
        v1_num, _ := strconv.Atoi(v1_slice[0])
        v1_slice = v1_slice[1:]
        if v1_num > 0 {
            return 1
        }
    }

    for len(v2_slice) > 0 {
        v2_num, _ := strconv.Atoi(v2_slice[0])
        v2_slice = v2_slice[1:]
        if v2_num > 0 {
            return -1
        }
    }

    return 0
}