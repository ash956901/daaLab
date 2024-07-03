def stable_match(men_pref,women_pref):
    num=len(men_pref)

    free_men=list(range(num))
    man_partner=[-1] * num
    woman_partner=[-1] * num
    proposals=[0]*num


    while free_men:
        man=free_men.pop(0)
        woman=men_pref[man][proposals[man]]
        proposals[man]+=1

        if woman_partner[woman] == -1:
            man_partner[man]=woman
            woman_partner[woman]=man

        else:
            current_partner=woman_partner[woman]
            woman_p=women_pref[woman]
            if woman_p.index(man)<woman_p.index(current_partner):
                woman_partner[woman]=man
                man_partner[man]=woman
                free_men.append(current_partner)
            else:
                free_men.append(man)
    
    return man_partner
