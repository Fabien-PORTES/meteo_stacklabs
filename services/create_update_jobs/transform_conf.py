CONF = [
    {
        "query": '''select
    data, id, mois, jour, annee, numero_de_message, temperature_partie_entiere, temperature_partie_decimale, humidite, pluie_en_augets, direction_du_vecteur_moyen_de_vent, force_moyenne_du_vecteur_de_vent, pression_a_decoder, direction_du_vecteur_de_vent_max, force_du_vecteur_de_vent_max, pluie_la_plus_intense_durant_1_min, type_station, pluie_intensite_max, heure, annee_reelle, minute, pression, temperature_decodee, direction_du_vecteur_vent_moyen, type_de_station, pluie, direction_du_vecteur_de_vent_max_en_degres, force_moyenne_du_vecteur_vent, force_rafale_max, jour_mois, dd_mm_yy_utc, hh_mm_utc, dd_mm_yy_hh_mm, temperature_en_degre_c, false_message, dd_mm_yy_hh_mm_utc, heure_paris_dd_mm_yy_hh_mm, heure_de_paris, heure_utc,
    to_timestamp(dd_mm_yy_hh_mm_utc) as record_timestamp
    from {datasource_0}''',
        'datasources': ["toulouse_34"],
        's3_folder': 'toulouse_34_cleaned',
        'table_name': 'toulouse_34_cleaned'
    },
    {
        "query": '''select
    data, bitype, sous_stat_data, 3rd_type, bithum, stat_type_2, stat_type_3, ss_hum_data, iss_data, id, mois, jour, annee, numero_de_message, temperature_partie_entiere, temperature_partie_decimale, humidite, pluie, direction_du_vecteur_moyen_de_vent, force_moyenne_du_vecteur_de_vent, pression, direction_du_vecteur_de_vent_max, force_du_vecteur_de_vent_max, pluie_la_plus_intense_durant_1_min, type_station, heure, annee_reelle, minute, pression_en_hpa, temperature_decodee, direction_du_vecteur_vent_moyen, type_de_station, pluie_en_mm, direction_du_vecteur_de_vent_max_en_degres, force_moyenne_du_vecteur_vent, force_rafale_max, mois_jour, mm_dd_yy, date_utc_yy_mm_dd_, mm_dd_yy_hh, mm_dd_yy_hh_mm, temperature_en_degre_c, ss_id, ss_mois, ss_jour, ss_annee, ss_numero_de_message, ss_heure, ss_minute, ss_annee_vraie, 1st_quarter_min, 2nd_quarter_hour, 2nd_quarter_minute, 3rd_quarter_hour, 3rd_quarter_minute, 2nd_quarter_hh_mm, 3rd_quarter_hh_mm, ss_jj_mm, ss_jj_mm_yy, ss_hh_mm, ss_jj_mm_yy_hh_mm, datetime_fuseau, 2nd_quarter_jj_mm_yy_hh_mm, 3rd_quarter_jj_mm_yy_hh_mm, bitsign_s1q1, sign_ss1_q1, temp_int_s1_q1, temp_dec_s1_q1, s1q1_sign_int, temp_s1_q1, bitsign_s2_q1, sign_s2_q1, temp_int_s2_q1, temp_dec_s2_q1, sign_tint_s2q1, temp_s2q1, bitsign_s3q1, sign_s3q1, tint_s3q1, tdec_s3q1, sign_tint_s3q1, temp_s3q1, bitsign_s1q2, sign_s1q2, tint_s1q2, tdec_s1q2, sign_tint_s1q2, temp_s1q2, bitsign_s2q2, sign_s2q2, tint_s2q2, tdec_s2q2, signtint_s2q2, temp_s2q2, bitsign_s3q2, sign_s3q2, tint_s3q2, tdec_s3q2, signtint_s3q2, temp_s3q2, bitsign_s1q3, signs_s1q3, tint_s1q3, tdec_s1q3, signtint_s1q3, temp_s1q3, bitsign_s2q3, sign_s2q3, tint_s2q3, tdec_s2q3, signtint_s2q3, temp_s2q3, bitsign_s3q3, sign_s3q3, tint_s3q3, tdec_s3q3, signtint_s3q3, temp_s3q3, ss_hum_id, ss_hum_mois, ss_hum_jour, ss_hum_an, ss_hum_annee, ss_hum_numsg, ss_hum_heure, ss_hum_minute, ss_hum_1st_half_min, ss_hum_2nd_half_min, ss_hum_3rd_half_min, ss_hum_4th_half_min, ss_hum_5th_half_min, ss_hum_6th_half_min, ss_hum_2nd_half_hour, ss_hum_2d_half_minute, ss_hum_3rd_half_hour, ss_hum_3rd_half_minute, ss_hum_4th_half_hour, ss_hum_4th_half_minute, ss_hum_5th_half_hour, ss_hum_5th_half_minute, ss_hum_6th_half_hour, ss_hum_6th_half_minute, ss_hum_jj_mm, ss_hum_jj_mm_yy, ss_hum_jj_mm_yy_t, ss_hum_1st_half, ss_hum_2nd_half, ss_hum_3rd_half, ss_hum_4th_half, ss_hum_5th_half, ss_hum_6th_half, hum_s1d1, hum_s2d1, hum_s1d2, hum_s2d2, hum_s1d3, hum_s2d3, hum_s1d4, hum_s2d4, hum_s1d5, hum_s2d5, hum_s1d6, hum_s2d6, 1st_half_data_hour, humidite_station_1_demi_heure_6, humidite_station_2_demi_heure_6, 2nd_half_data_hour, humidite_station_1_demi_heure_5, humidite_station_2_demi_heure_5, 3rd_half_data_hour, humidite_station_1_demi_heure_4, humidite_station_2_demi_heure_4, 4th_half_data_hour, humidite_station_1_demi_heure_3, humidite_station_2_demi_heure_3, 5th_half_data_hour, humidite_station_1_demi_heure_2, humidite_station_2_demi_heure_2, 6th_half_data_hour, humidite_station_1_demi_heure_1, humidite_station_2_demi_heure_1,
    to_timestamp(mm_dd_yy_hh_mm) as record_timestamp
    from {datasource_0}
    WHERE type_de_station != 'sous station' ''',
        'datasources': ["toulouse_6"],
        's3_folder': 'toulouse_6_cleaned',
        'table_name': 'toulouse_6_cleaned'
    },
    {
        "query": '''select
    data, bitype, sous_stat_data, 3rd_type, bithum, stat_type_2, stat_type_3, ss_hum_data, iss_data, id, mois, jour, annee, numero_de_message, temperature_partie_entiere, temperature_partie_decimale, humidite, pluie, direction_du_vecteur_moyen_de_vent, force_moyenne_du_vecteur_de_vent, pression, direction_du_vecteur_de_vent_max, force_du_vecteur_de_vent_max, pluie_la_plus_intense_durant_1_min, type_station, heure, annee_reelle, minute, pression_en_hpa, temperature_decodee, direction_du_vecteur_vent_moyen, type_de_station, pluie_en_mm, direction_du_vecteur_de_vent_max_en_degres, force_moyenne_du_vecteur_vent, force_rafale_max, mois_jour, mm_dd_yy, date_utc_yy_mm_dd_, mm_dd_yy_hh, mm_dd_yy_hh_mm, temperature_en_degre_c, ss_id, ss_mois, ss_jour, ss_annee, ss_numero_de_message, ss_heure, ss_minute, ss_annee_vraie, 1st_quarter_min, 2nd_quarter_hour, 2nd_quarter_minute, 3rd_quarter_hour, 3rd_quarter_minute, 2nd_quarter_hh_mm, 3rd_quarter_hh_mm, ss_jj_mm, ss_jj_mm_yy, ss_hh_mm, ss_jj_mm_yy_hh_mm, datetime_fuseau, 2nd_quarter_jj_mm_yy_hh_mm, 3rd_quarter_jj_mm_yy_hh_mm, bitsign_s1q1, sign_ss1_q1, temp_int_s1_q1, temp_dec_s1_q1, s1q1_sign_int, temp_s1_q1, bitsign_s2_q1, sign_s2_q1, temp_int_s2_q1, temp_dec_s2_q1, sign_tint_s2q1, temp_s2q1, bitsign_s3q1, sign_s3q1, tint_s3q1, tdec_s3q1, sign_tint_s3q1, temp_s3q1, bitsign_s1q2, sign_s1q2, tint_s1q2, tdec_s1q2, sign_tint_s1q2, temp_s1q2, bitsign_s2q2, sign_s2q2, tint_s2q2, tdec_s2q2, signtint_s2q2, temp_s2q2, bitsign_s3q2, sign_s3q2, tint_s3q2, tdec_s3q2, signtint_s3q2, temp_s3q2, bitsign_s1q3, signs_s1q3, tint_s1q3, tdec_s1q3, signtint_s1q3, temp_s1q3, bitsign_s2q3, sign_s2q3, tint_s2q3, tdec_s2q3, signtint_s2q3, temp_s2q3, bitsign_s3q3, sign_s3q3, tint_s3q3, tdec_s3q3, signtint_s3q3, temp_s3q3, ss_hum_id, ss_hum_mois, ss_hum_jour, ss_hum_an, ss_hum_annee, ss_hum_numsg, ss_hum_heure, ss_hum_minute, ss_hum_1st_half_min, ss_hum_2nd_half_min, ss_hum_3rd_half_min, ss_hum_4th_half_min, ss_hum_5th_half_min, ss_hum_6th_half_min, ss_hum_2nd_half_hour, ss_hum_2d_half_minute, ss_hum_3rd_half_hour, ss_hum_3rd_half_minute, ss_hum_4th_half_hour, ss_hum_4th_half_minute, ss_hum_5th_half_hour, ss_hum_5th_half_minute, ss_hum_6th_half_hour, ss_hum_6th_half_minute, ss_hum_jj_mm, ss_hum_jj_mm_yy, ss_hum_jj_mm_yy_t, ss_hum_1st_half, ss_hum_2nd_half, ss_hum_3rd_half, ss_hum_4th_half, ss_hum_5th_half, ss_hum_6th_half, hum_s1d1, hum_s2d1, hum_s1d2, hum_s2d2, hum_s1d3, hum_s2d3, hum_s1d4, hum_s2d4, hum_s1d5, hum_s2d5, hum_s1d6, hum_s2d6, 1st_half_data_hour, humidite_station_1_demi_heure_6, humidite_station_2_demi_heure_6, 2nd_half_data_hour, humidite_station_1_demi_heure_5, humidite_station_2_demi_heure_5, 3rd_half_data_hour, humidite_station_1_demi_heure_4, humidite_station_2_demi_heure_4, 4th_half_data_hour, humidite_station_1_demi_heure_3, humidite_station_2_demi_heure_3, 5th_half_data_hour, humidite_station_1_demi_heure_2, humidite_station_2_demi_heure_2, 6th_half_data_hour, humidite_station_1_demi_heure_1, humidite_station_2_demi_heure_1,
    to_timestamp(mm_dd_yy_hh_mm) as record_timestamp
    from {datasource_0}
    WHERE type_de_station != 'sous station' ''',
        'datasources': ["toulouse_65"],
        's3_folder': 'toulouse_65_cleaned',
        'table_name': 'toulouse_65_cleaned'
    },
    {
        "query": '''select
    data, bitype, sous_stat_data, 3rd_type, bithum, stat_type_2, stat_type_3, ss_hum_data, iss_data, id, mois, jour, annee, numero_de_message, temperature_partie_entiere, temperature_partie_decimale, humidite, pluie, direction_du_vecteur_moyen_de_vent, force_moyenne_du_vecteur_de_vent, pression, direction_du_vecteur_de_vent_max, force_du_vecteur_de_vent_max, pluie_la_plus_intense_durant_1_min, type_station, heure, annee_reelle, minute, pression_en_hpa, temperature_decodee, direction_du_vecteur_vent_moyen, type_de_station, pluie_en_mm, direction_du_vecteur_de_vent_max_en_degres, force_moyenne_du_vecteur_vent, force_rafale_max, mois_jour, mm_dd_yy, date_utc_yy_mm_dd_, mm_dd_yy_hh, mm_dd_yy_hh_mm, temperature_en_degre_c, ss_id, ss_mois, ss_jour, ss_annee, ss_numero_de_message, ss_heure, ss_minute, ss_annee_vraie, 1st_quarter_min, 2nd_quarter_hour, 2nd_quarter_minute, 3rd_quarter_hour, 3rd_quarter_minute, 2nd_quarter_hh_mm, 3rd_quarter_hh_mm, ss_jj_mm, ss_jj_mm_yy, ss_hh_mm, ss_jj_mm_yy_hh_mm, datetime_fuseau, 2nd_quarter_jj_mm_yy_hh_mm, 3rd_quarter_jj_mm_yy_hh_mm, bitsign_s1q1, sign_ss1_q1, temp_int_s1_q1, temp_dec_s1_q1, s1q1_sign_int, temp_s1_q1, bitsign_s2_q1, sign_s2_q1, temp_int_s2_q1, temp_dec_s2_q1, sign_tint_s2q1, temp_s2q1, bitsign_s3q1, sign_s3q1, tint_s3q1, tdec_s3q1, sign_tint_s3q1, temp_s3q1, bitsign_s1q2, sign_s1q2, tint_s1q2, tdec_s1q2, sign_tint_s1q2, temp_s1q2, bitsign_s2q2, sign_s2q2, tint_s2q2, tdec_s2q2, signtint_s2q2, temp_s2q2, bitsign_s3q2, sign_s3q2, tint_s3q2, tdec_s3q2, signtint_s3q2, temp_s3q2, bitsign_s1q3, signs_s1q3, tint_s1q3, tdec_s1q3, signtint_s1q3, temp_s1q3, bitsign_s2q3, sign_s2q3, tint_s2q3, tdec_s2q3, signtint_s2q3, temp_s2q3, bitsign_s3q3, sign_s3q3, tint_s3q3, tdec_s3q3, signtint_s3q3, temp_s3q3, ss_hum_id, ss_hum_mois, ss_hum_jour, ss_hum_an, ss_hum_annee, ss_hum_numsg, ss_hum_heure, ss_hum_minute, ss_hum_1st_half_min, ss_hum_2nd_half_min, ss_hum_3rd_half_min, ss_hum_4th_half_min, ss_hum_5th_half_min, ss_hum_6th_half_min, ss_hum_2nd_half_hour, ss_hum_2d_half_minute, ss_hum_3rd_half_hour, ss_hum_3rd_half_minute, ss_hum_4th_half_hour, ss_hum_4th_half_minute, ss_hum_5th_half_hour, ss_hum_5th_half_minute, ss_hum_6th_half_hour, ss_hum_6th_half_minute, ss_hum_jj_mm, ss_hum_jj_mm_yy, ss_hum_jj_mm_yy_t, ss_hum_1st_half, ss_hum_2nd_half, ss_hum_3rd_half, ss_hum_4th_half, ss_hum_5th_half, ss_hum_6th_half, hum_s1d1, hum_s2d1, hum_s1d2, hum_s2d2, hum_s1d3, hum_s2d3, hum_s1d4, hum_s2d4, hum_s1d5, hum_s2d5, hum_s1d6, hum_s2d6, 1st_half_data_hour, humidite_station_1_demi_heure_6, humidite_station_2_demi_heure_6, 2nd_half_data_hour, humidite_station_1_demi_heure_5, humidite_station_2_demi_heure_5, 3rd_half_data_hour, humidite_station_1_demi_heure_4, humidite_station_2_demi_heure_4, 4th_half_data_hour, humidite_station_1_demi_heure_3, humidite_station_2_demi_heure_3, 5th_half_data_hour, humidite_station_1_demi_heure_2, humidite_station_2_demi_heure_2, 6th_half_data_hour, humidite_station_1_demi_heure_1, humidite_station_2_demi_heure_1,
    to_timestamp(mm_dd_yy_hh_mm) as record_timestamp
    from {datasource_0}
    WHERE type_de_station != 'sous station' ''',
        'datasources': ["toulouse_66"],
        's3_folder': 'toulouse_66_cleaned',
        'table_name': 'toulouse_66_cleaned'
    },
    {
        "query": '''select
    data, bitype, sous_stat_data, 3rd_type, bithum, stat_type_2, stat_type_3, ss_hum_data, iss_data, id, mois, jour, annee, numero_de_message, temperature_partie_entiere, temperature_partie_decimale, humidite, pluie, direction_du_vecteur_moyen_de_vent, force_moyenne_du_vecteur_de_vent, pression, direction_du_vecteur_de_vent_max, force_du_vecteur_de_vent_max, pluie_la_plus_intense_durant_1_min, type_station, heure, annee_reelle, minute, pression_en_hpa, temperature_decodee, direction_du_vecteur_vent_moyen, type_de_station, pluie_en_mm, direction_du_vecteur_de_vent_max_en_degres, force_moyenne_du_vecteur_vent, force_rafale_max, mois_jour, mm_dd_yy, date_utc_yy_mm_dd_, mm_dd_yy_hh, mm_dd_yy_hh_mm, temperature_en_degre_c, ss_id, ss_mois, ss_jour, ss_annee, ss_numero_de_message, ss_heure, ss_minute, ss_annee_vraie, 1st_quarter_min, 2nd_quarter_hour, 2nd_quarter_minute, 3rd_quarter_hour, 3rd_quarter_minute, 2nd_quarter_hh_mm, 3rd_quarter_hh_mm, ss_jj_mm, ss_jj_mm_yy, ss_hh_mm, ss_jj_mm_yy_hh_mm, datetime_fuseau, 2nd_quarter_jj_mm_yy_hh_mm, 3rd_quarter_jj_mm_yy_hh_mm, bitsign_s1q1, sign_ss1_q1, temp_int_s1_q1, temp_dec_s1_q1, s1q1_sign_int, temp_s1_q1, bitsign_s2_q1, sign_s2_q1, temp_int_s2_q1, temp_dec_s2_q1, sign_tint_s2q1, temp_s2q1, bitsign_s3q1, sign_s3q1, tint_s3q1, tdec_s3q1, sign_tint_s3q1, temp_s3q1, bitsign_s1q2, sign_s1q2, tint_s1q2, tdec_s1q2, sign_tint_s1q2, temp_s1q2, bitsign_s2q2, sign_s2q2, tint_s2q2, tdec_s2q2, signtint_s2q2, temp_s2q2, bitsign_s3q2, sign_s3q2, tint_s3q2, tdec_s3q2, signtint_s3q2, temp_s3q2, bitsign_s1q3, signs_s1q3, tint_s1q3, tdec_s1q3, signtint_s1q3, temp_s1q3, bitsign_s2q3, sign_s2q3, tint_s2q3, tdec_s2q3, signtint_s2q3, temp_s2q3, bitsign_s3q3, sign_s3q3, tint_s3q3, tdec_s3q3, signtint_s3q3, temp_s3q3, ss_hum_id, ss_hum_mois, ss_hum_jour, ss_hum_an, ss_hum_annee, ss_hum_numsg, ss_hum_heure, ss_hum_minute, ss_hum_1st_half_min, ss_hum_2nd_half_min, ss_hum_3rd_half_min, ss_hum_4th_half_min, ss_hum_5th_half_min, ss_hum_6th_half_min, ss_hum_2nd_half_hour, ss_hum_2d_half_minute, ss_hum_3rd_half_hour, ss_hum_3rd_half_minute, ss_hum_4th_half_hour, ss_hum_4th_half_minute, ss_hum_5th_half_hour, ss_hum_5th_half_minute, ss_hum_6th_half_hour, ss_hum_6th_half_minute, ss_hum_jj_mm, ss_hum_jj_mm_yy, ss_hum_jj_mm_yy_t, ss_hum_1st_half, ss_hum_2nd_half, ss_hum_3rd_half, ss_hum_4th_half, ss_hum_5th_half, ss_hum_6th_half, hum_s1d1, hum_s2d1, hum_s1d2, hum_s2d2, hum_s1d3, hum_s2d3, hum_s1d4, hum_s2d4, hum_s1d5, hum_s2d5, hum_s1d6, hum_s2d6, 1st_half_data_hour, humidite_station_1_demi_heure_6, humidite_station_2_demi_heure_6, 2nd_half_data_hour, humidite_station_1_demi_heure_5, humidite_station_2_demi_heure_5, 3rd_half_data_hour, humidite_station_1_demi_heure_4, humidite_station_2_demi_heure_4, 4th_half_data_hour, humidite_station_1_demi_heure_3, humidite_station_2_demi_heure_3, 5th_half_data_hour, humidite_station_1_demi_heure_2, humidite_station_2_demi_heure_2, 6th_half_data_hour, humidite_station_1_demi_heure_1, humidite_station_2_demi_heure_1,
    to_timestamp(mm_dd_yy_hh_mm) as record_timestamp
    from {datasource_0}
    WHERE type_de_station != 'sous station' ''',
        'datasources': ["toulouse_63"],
        's3_folder': 'toulouse_63_cleaned',
        'table_name': 'toulouse_63_cleaned'
    },
    {
        "query": '''select
    data, id, mois, jour, annee, numero_de_message, temperature_partie_entiere, temperature_partie_decimale, humidite, pluie_en_augets, direction_du_vecteur_moyen_de_vent, force_moyenne_du_vecteur_de_vent, pression_a_decoder, direction_du_vecteur_de_vent_max, force_du_vecteur_de_vent_max, pluie_la_plus_intense_durant_1_min, type_station, pluie_intensite_max, heure, annee_reelle, minute, pression, temperature_decodee, direction_du_vecteur_vent_moyen, type_de_station, pluie, direction_du_vecteur_de_vent_max_en_degres, force_moyenne_du_vecteur_vent, force_rafale_max, jour_mois, dd_mm_yy_utc, hh_mm_utc, dd_mm_yy_hh_mm, temperature_en_degre_c, false_message, dd_mm_yy_hh_mm_utc, heure_paris_dd_mm_yy_hh_mm, heure_de_paris, heure_utc,
    to_timestamp(dd_mm_yy_hh_mm_utc) as record_timestamp
    from {datasource_0}''',
        'datasources': ["toulouse_48"],
        's3_folder': 'toulouse_48_cleaned',
        'table_name': 'toulouse_48_cleaned'
    },
    {"query": '''select
                record_timestamp,
                id,
                temperature_en_degre_c,
                pluie,
                humidite
                from {datasource_0}
                UNION ALL
                select
                record_timestamp,
                id,
                temperature_en_degre_c,
                pluie,
                humidite
                from {datasource_1}
                UNION ALL
                select
                record_timestamp,
                id,
                temperature_en_degre_c,
                pluie,
                humidite
                from {datasource_2}
                UNION ALL
                select
                record_timestamp,
                id,
                temperature_en_degre_c,
                pluie,
                humidite
                from {datasource_3}
                UNION ALL
                select
                record_timestamp,
                id,
                temperature_en_degre_c,
                pluie,
                humidite
                from {datasource_4}
                UNION ALL
                select
                record_timestamp,
                id,
                temperature_en_degre_c,
                pluie,
                humidite
                from {datasource_5}''',
     'datasources': ["toulouse_34_cleaned", "toulouse_48_cleaned", "toulouse_6_cleaned", "toulouse_63_cleaned", "toulouse_65_cleaned", "toulouse_66_cleaned"],
     's3_folder': 'all_station',
     'table_name': 'all_station'
     },
    {
        "query": '''SELECT CAST(record_timestamp AS date) AS date,
         id,
         min(temperature_en_degre_c) AS min_temp,
         max(temperature_en_degre_c) AS max_temp,
         min(humidite) AS min_humidite,
         max(humidite) AS max_humidite
FROM all_station
GROUP BY  CAST(record_timestamp AS date), id''',
        'datasources': ["all_station"],
        's3_folder': 'station_aggregate',
        'table_name': 'station_aggregate'
    }
]
