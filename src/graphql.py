query = """query($page: Int) {
                reportData {
                    reports(zoneID: 1020, page: $page) {
                        total
                        per_page
                        current_page
                        has_more_pages
                        data {
                            code
                            fights {
                                name
                                bossPercentage
                                encounterID
                                kill
                            }
                        }
                    }
                }
            }"""
